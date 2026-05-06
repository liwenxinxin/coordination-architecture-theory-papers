# Mode 1 — Direct Human Labor: Standalone Treatment of the First Labor Mode in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize the first of the three labor modes in the CKS labor allocation framework — **Mode 1, direct human labor** — as a standalone architectural specification with independent operational content, separable from Mode 2 (LLM labor under orchestration rules) and Mode 3 (stable-cell automation), with which it composes within the framework.

## Abstract

The Coordination Knowledge Substrate (CKS) labor allocation framework names three modes by which coordination work can be performed: Mode 1 (humans operating directly on substrate), Mode 2 (LLMs under human-authored orchestration rules), and Mode 3 (stable cells executing under rules whose stability has reduced per-execution human attention to near zero). A separate foundational note formalizes the framework as a whole; an integrating-frame operational note names the three modes alongside the architectural properties that make their coexistence coherent. This note formalizes Mode 1 specifically — direct human labor — as having independent architectural content: the human's direct work over substrate, reading content directly via the inspect right, writing content directly via the modify or override rights, producing substrate writes whose provenance carries human writer attribution, all without rule-mediation as a precondition. The note states the four operational components that constitute Mode 1, distinguishes the standalone treatment from positions stronger than the source paper supports, separates Mode 1 from four adjacent labor patterns commonly conflated with it, names the connections that make Mode 1 load-bearing for several other CKS commitments, enumerates ten failure modes grouped by violation mechanism, and provides an operational test for whether a system instantiates Mode 1 in the architectural sense.

## 1. Why Mode 1 needs to be formalized as standalone

The labor allocation framework's foundational note establishes the three modes as a single architectural property of CKS, and an integrating-frame operational note names Mode 1 alongside its sibling modes, the three architectural properties (single substrate, mode-independent authority, attributable writer) that make the modes coherent on a single substrate, and the labor-vs-authority distinction. Across both treatments, Mode 1 is named as one of three modes; its content is articulated in the company of the other two.

That joint framing leaves a class of cases architecturally underspecified. Several common deployment situations require direct human labor regardless of whether Mode 2 or Mode 3 are operationally available: a deployment at start, before any orchestration rules have been authored; a decision outside the scope of any authored rule; an override action exercised without rule-justification as a precondition; a direct-judgment moment where the human has decided that rule-mediated work is inadequate. In each case, the labor is Mode 1 specifically — direct human work, with substrate writes carrying human writer attribution — and the architecture's commitment to Mode 1 must be defensible as a property of its design, not as a fortunate consequence of which modes happen to be available.

Naming Mode 1 as a standalone architectural commitment makes Mode 1 describable as the foundational mode the labor allocation framework rests on, prevents the slide into "all coordination work must eventually be cell-mediated" misreadings, and connects the mode to the human-governed commitment's three rights. The three rights — inspect, modify, override — are exercised through Mode 1 directly. Mode 2 and Mode 3 do not exercise the rights; they are LLM and cell labor under orchestration rules, with the rights reserved for human exercise. Without Mode 1 as a standalone architectural mode, the rights would be exercisable only through Mode 2 or Mode 3 mediation — a position the source paper does not commit to.

## 2. The Mode 1 commitment, defined

A system supports **Mode 1 — direct human labor** when humans can perform coordination work on substrate directly, with the labor producing substrate writes attributed to the human writer, without rule-mediation as a precondition. The commitment has four operational components.

**(a) Direct read operations.** Humans with appropriate access can read substrate content and orchestration-rule content directly, in inspectable form, without LLM intermediation as a precondition. Reads are non-mutating; the labor is the human's direct inspection. Read operations under Mode 1 are subject to the substrate's read-determinism guarantees — the same substrate state produces the same content for the human reader as for any other reader — making Mode 1 reads observationally consistent with reads in any other mode.

**(b) Direct write operations.** Humans with appropriate access can modify or override substrate content directly, producing substrate writes that cross the substrate boundary as atomic operations carrying provenance. The modify action alters existing content; the override action substitutes different content; both produce writes the substrate carries until written again under appropriate authority. The labor is the human's direct production of substrate content.

**(c) Human writer attribution.** Substrate writes produced by Mode 1 labor carry **human writer attribution** in their provenance. The writer field identifies the human as the writer; no orchestration rule is named as the producing rule, and no cell as the producing cell. This distinguishes Mode 1 writes from Mode 2 writes (cell-with-rule attribution) and Mode 3 writes (stable-cell attribution). Any reader, in any later cell execution, can determine that a piece of content was written in Mode 1 by inspecting its provenance.

**(d) No rule-mediation requirement.** Mode 1 labor does not require an orchestration rule to be in scope as a precondition. Humans exercise the inspect, modify, and override rights directly, without first consulting, justifying against, or conforming to a rule. This distinguishes Mode 1 from Mode 2 architecturally: in Mode 2, an orchestration rule is present and the LLM operates under it; in Mode 1, no rule mediates the human's work, and no rule needs to be present for the work to be architecturally admissible. Cells without rule-governance — cells the human executes as tooling without an orchestration rule constraining them — are not Mode 2 labor; they are cell-tooling that supports Mode 1.

The four components together constitute Mode 1 as an architectural mode. A system that supports all four supports Mode 1; a system that fails any of the four does not, regardless of whether direct human labor occurs in the system in some other operational sense.

## 3. What the Mode 1 commitment does NOT claim

The standalone treatment is not maximalist. Stating precisely what Mode 1 does not claim is what keeps the framing from drifting beyond what the source paper supports.

**It does not claim humans never use cells in Mode 1.** Humans may execute cells operationally — running a cell to perform a query, transformation, or retrieval as part of their direct work. If the human is the substrate writer per the provenance, the labor is Mode 1; the cell is tooling. The architectural distinction lives at the writer-attribution level, not at the operational-tooling level.

**It does not claim Mode 1 is preferable to Mode 2 or Mode 3.** The architecture is mode-agnostic at the architectural-commitment level. Specific deployments may have preferences based on operational concerns; those preferences are deployment choices the architecture does not constrain.

**It does not foreclose Mode 1 humans from authoring orchestration rules.** The same human may exercise Mode 1 labor at one moment and exercise rule authoring at another. Mode 1 is a labor category, not an authorship category; the two are distinct activities.

**It does not require Mode 1 to be the only mode in any deployment.** The architectural commitment is that Mode 1 is operationally available, not that it is exclusive. A deployment in which most substrate writes are produced in Mode 3 is still a fully Mode-1-supporting deployment, provided the four components hold for the Mode 1 work that does occur.

**It does not specify which decisions should be performed in Mode 1.** Specific decision-mode allocations are deployment choices; the architectural commitment is to the mode being available for any decision the deployment chooses to allocate to it.

**It does not foreclose deployment-level features that support Mode 1.** Deployments may build interfaces, editing tools, or workflows that enhance Mode 1's operational experience. The architectural commitment is to direct human labor being feasible — to the four components holding — not to any specific feature being present.

## 4. What Mode 1 is NOT

Four adjacent labor patterns are commonly conflated with Mode 1. Each is real and reasonable in some other architecture; naming what Mode 1 is not is what prevents the misreading.

**Not manual data entry.** Manual data entry names the operational activity of humans typing data into systems. Mode 1 is broader: it includes any direct human labor that produces substrate writes, regardless of entry mechanism — pasting, importing, bulk-updating through commodity tools, or committing query results as writes are all Mode 1 when the human is the substrate writer per the provenance. The architectural distinction is at the labor-mode level, not the data-entry-mechanism level.

**Not traditional human-only workflows.** Traditional human-only workflows are coordination patterns in which all work is performed by humans, with no LLM involvement and no automated cells. Mode 1 is one of three labor modes within the CKS framework; the architecture supports Mode 1 alongside Mode 2 and Mode 3. Implementations that present CKS as requiring human-only labor over-claim Mode 1 and miss the framework's mode-allocation flexibility.

**Not single-user systems.** Single-user systems are operational patterns in which one human is the user. Mode 1 is mode-agnostic about user count; multi-human deployments may have multiple humans simultaneously operating in Mode 1, each producing substrate writes with their own writer attribution. The architectural distinction is at the labor-mode level, not the user-count level.

**Not expert-only systems.** Expert-only systems are operational patterns in which only specialists perform coordination work. Mode 1 is accessibility-agnostic: the non-specialist governance commitment makes Mode 1 exercisable by any human within whose authority scope the work falls, in commodity tools satisfying the tool-agnosticism requirements. The misreading "Mode 1 = expert direct labor" inherits from systems in which direct manipulation requires specialist tooling; Mode 1 in CKS does not.

## 5. Why Mode 1 is load-bearing for downstream commitments

Mode 1 carries weight for several other CKS commitments. Naming the connections precisely is what makes the standalone treatment defensible as more than terminological — Mode 1 is the mode without which the connected commitments do not stand.

**The labor allocation framework.** Mode 1 is one of the three modes; without it, the framework would consist of LLM-under-rule and stable-cell labor only. Mode 2 and Mode 3 are both rule-mediated; a framework that does not name a non-rule-mediated mode cannot represent the work that occurs before any rule has been authored or outside any rule's scope.

**The human-governed commitment.** The three rights are exercised through Mode 1 directly. Without Mode 1, the rights would be exercised only through Mode 2 or Mode 3 mediation, which would mean the rights are mediated rather than direct. The human-governed commitment is to authority "at any time" without architectural intermediaries; Mode 1 is the mode that operationalizes the at-any-time exercisability.

**The override commitment.** Override is a Mode 1 operation by definition — humans override substrate content directly, without rule-justification as a precondition. Without Mode 1, override would have to be mediated through cells operating under rules, which would compromise the no-justification-as-precondition property. The Moment 2 governance moment is exactly Mode 1 labor exercising the override right.

**Mode progression dynamics.** Mode 1 is the starting point for typical mode progression. A team begins entirely in Mode 1; as patterns emerge in the human's work, the team authors orchestration rules and work moves to Mode 2; as rules stabilize, Mode 3 becomes available. Mode 1 remains operationally present at every later stage. Without Mode 1 as a foundational mode, the progression has no starting point and the architecture's bottom-up adoption profile collapses.

**Non-specialist governance.** Non-specialists exercise governance through Mode 1 labor — directly inspecting, modifying, or overriding substrate content in commodity tools they already use. Without Mode 1, non-specialist governance would require Mode 2 or Mode 3 mediation, re-introducing the specialist requirement (rule-authoring expertise, cell-execution expertise) that the non-specialist governance commitment removes. Mode 1 is what makes non-specialist governance exercisable rather than only nominal.

## 6. Failure modes that violate Mode 1

A system can fail Mode 1 specifically, even when it satisfies parts of the broader labor allocation framework or the human-governed commitment. Ten failure modes name the most common ways this happens, grouped here by violation mechanism.

**Cell-mediation violations.** Three failure modes route what should be direct human labor through cell architecture.

(a) **Mandatory cell-mediation.** The implementation requires all substrate writes to go through cells, with no direct human write path. Mode 1 is architecturally absent because direct human labor is not operationally feasible.

(b) **Mode 1 with hidden cell-mediation.** The implementation claims Mode 1 capability but operationally routes human writes through hidden cells with implicit rules. The architectural commitment is nominally present but operationally violated; writer attribution may show "human" while the substrate write was actually produced by a cell the human triggered.

(c) **Mode-1-only systems.** The implementation is operationally capable only of Mode 1; Mode 2 and Mode 3 are absent. The system is not Mode-1-supporting but Mode-1-imposing; the labor allocation framework is not present, and the system loses the labor-allocation flexibility that makes Mode 1 a mode rather than a constraint.

**Rule-mediation violations.** Three failure modes import rule-mediation requirements into work that should be direct.

(d) **Mandatory rule-justification for human writes.** The implementation requires humans to provide rule references, conformance proofs, or rule-derivation arguments for all writes. Direct human labor is constrained by rule-mediation requirements that the override-without-justification commitment forbids; Mode 1 is conflated with Mode 2.

(e) **Mandatory approval workflows for human writes.** The implementation requires approval workflows — review gates, sign-off chains, designated-reviewer queues — for all human writes, blocking direct exercise of the modify or override rights. Governance becomes procedural rather than architectural; the at-any-time exercisability fails.

(f) **Implicit Mode 2 promotion.** The implementation treats frequent Mode 1 patterns as automatically promoting to Mode 2 by generating rules from observed human work without an authorship moment. Rules accrete without human authorship; what was Mode 1 labor becomes Mode 2 labor by accretion rather than by deliberate transition.

**Attribution and access violations.** Two failure modes compromise the writer attribution that distinguishes the modes or the access that makes Mode 1 exercisable.

(g) **Mode 1 attribution stripping.** The implementation does not distinguish Mode 1 writer attribution from Mode 2 or Mode 3 attribution. The three modes become indistinguishable at the substrate-content level; the framework loses the operational distinctness that the attributable-writer property guarantees.

(h) **Mode 1 with rule-bypass mechanisms.** The implementation provides Mode 1 capability through "rule-bypass" mechanisms that themselves require expertise to use — privileged accounts, escape-hatch tools, debug interfaces, vendor-supported override channels. Direct human labor is technically possible but operationally blocked for non-specialists; the accessibility commitment fails.

**Scale violations.** Two failure modes compromise Mode 1 specifically as substrate or deployment grows.

(i) **Mode 1 cost amplification.** The implementation requires Mode 1 labor to scale linearly with substrate size — for example, requiring humans to review every prior substrate change before any new write commits, or requiring per-element validation against the existing substrate. The architectural commitment to non-size-proportional governance fails specifically for Mode 1.

(j) **Mode 1 disablement at scale.** The implementation operationally disables Mode 1 once substrate reaches a certain size, claiming that "at scale" all work must be cell-mediated. The at-any-time exercisability becomes contingent on substrate size.

A system that exhibits any of (a)–(j) does not implement Mode 1 in the architectural sense, and naming the failure precisely is what allows downstream remediation.

## 7. Operational test

A system supports Mode 1 in the architectural sense if and only if all of the following are true at all times during the substrate's existence:

1. Direct read operations are operationally available — a human with appropriate access can read substrate content and orchestration-rule content directly, in inspectable form, without LLM intermediation as a precondition.
2. Direct write operations are operationally available — a human with appropriate access can modify or override substrate content directly, with the change taking effect as substrate state.
3. Substrate writes produced by direct human labor carry human writer attribution in their provenance, distinguishable from cell-with-rule attribution and stable-cell attribution.
4. No rule-mediation requirement applies as a precondition for direct human labor — humans exercise the inspect, modify, and override rights without first justifying their actions against an orchestration rule.
5. Mode 1 operates alongside Mode 2 and Mode 3; the deployment is not constrained to Mode 1 exclusively, and the labor allocation framework as a whole is implemented.
6. Mode 1 cost scales with intervention frequency (a deployment choice), not with substrate size; the at-any-time exercisability of Mode 1 does not degrade as substrate grows.

A system that fails any of (1)–(6) does not support Mode 1 in the architectural sense, even if humans appear to perform some direct labor in it operationally. Such a system may be a useful system, and may support some labor mode that resembles Mode 1 in surface respects, but it is not CKS-coherent on the Mode 1 axis, and downstream work that relies on its Mode 1 guarantees should be scoped accordingly.

## 8. Conclusion

Implementations under pressure to deliver "AI coordination" value drift toward cell-mediated patterns that compromise direct human labor. The drift is steady because cell-mediation is rhetorically associated with "AI" and with scalability, while direct human labor is sometimes positioned as primitive or non-AI. The positioning misses what the architectural commitment names. Mode 1 is not a placeholder for unautomated work; it is the mode in which humans exercise the three rights directly, the foundation that mode progression starts from, the mode that remains operationally present for decisions outside rule scope and for overrides, and the mode that makes non-specialist governance exercisable rather than only nominal.

Naming Mode 1 as a standalone architectural specification — with the four operational components, the limits on the standalone treatment, the four adjacent-pattern distinctions, the load-bearing connections, the ten failure modes grouped by mechanism, and the six-condition operational test — gives downstream readers a precise specification of what direct human labor architecturally requires, separable from the integrating-frame treatment of the labor allocation framework as a whole. Companion notes specialize Mode 2 and Mode 3 as siblings, the three architectural properties that hold across the modes, the labor-vs-authority distinction, and the mode progression dynamics; together they give the full operational decomposition of the labor allocation framework. The standalone treatment of Mode 1 is the foundation on which that decomposition rests.

Subsequent work that adopts the CKS pattern, extends it, or argues against it should use "Mode 1 — direct human labor" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Mode 1 — Direct Human Labor: Standalone Treatment of the First Labor Mode in the Coordination Knowledge Substrate Pattern.* 5 May 2026. ORCID: 0009-0004-8065-3235.
