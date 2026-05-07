# Cross-Partner Rule Authoring Conflict During Composition: A Boundary Case in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one boundary case for multi-substrate composition — the case in which humans at different composition partners author conflicting orchestration rules in close temporal proximity, producing a rule conflict that spans the authority boundaries of the participating partners — and to specify the architectural treatment that resolves the boundary in continuity with the source paper's commitments.

## Abstract

The CKS source paper commits orchestration rules at each substrate to human authoring under that substrate's governance (§3.3), and any multi-substrate composition to preserving per-substrate human governance, conflict preservation across boundaries, and addressable provenance (§13.3, formalized previously as five composition requirements). When two composition partners are operated by humans in different governance scopes, parallel rule authoring is the default: humans at partner A and partner B each author rules per Moment 1, and if their specifications disagree on operations that span the partners, the resulting rule conflict has no within-partner resolution. This note formalizes that boundary as standalone architectural treatment. Each partner's rule remains substrate-resident authoritative content within that partner; the cross-partner conflict is registered as a first-class substrate object with provenance distinguishing the partners' authors; resolution requires a meta-rule authored by humans whose authority is recorded as spanning the partners; until cross-partner authority is established, partner-internal rules govern affected operations through fail-defer-default behavior. The note names the four legitimate authority-spanning patterns, the eight anti-pattern resolutions the architecture excludes, and an operational test.

## 1. Why this boundary case needs a standalone formalization

The CKS source paper defends rule authoring as one of the two moments at which governance is exercised: humans write the orchestration rules that govern cell-level behavior, paid once per rule rather than once per cell execution (§3.3, §6.3). The composition-requirements derivation note formalizes the companion commitment from §13.3: any multi-substrate composition must preserve per-substrate human governance, with each substrate retaining the authority over its content and rules that the single-substrate case requires. These commitments compose without difficulty when each substrate's rules are written by humans within a single governance scope. They begin to interact non-trivially when two substrates participate in the same workflow, each carries human-authored rules per Moment 1, and the rules' specifications for operations that cross the boundary between them disagree: no within-partner human has authority that reaches the other partner.

The case is not exotic. Cross-partner deployments — multiple substrates aggregated into a workflow that operates across organizational, departmental, or federation boundaries — are a frequent operational form, and parallel rule authoring is the default mode of work in such deployments because rule authoring is governance and each partner's humans are exercising governance within their own scope. Standalone formalization separates this case from three adjacent boundary cases the architecture already addresses: the within-partner rule-conflict boundary, where partner-internal authority resolves the conflict; the authority-distribution-change boundary, where humans alter who has what authority and rule conflicts are a downstream effect; and the substrate concurrent-write race boundary, where the conflict is at the data layer rather than the rule layer. Naming the cross-partner case explicitly is what prevents implementers from mapping it onto an adjacent case and applying the wrong response.

## 2. The boundary scenario

Five properties together distinguish the scenario. First, two composition partners participate in a multi-substrate composition that satisfies the composition requirements at the time of conflict; each is human-governed in the source paper's sense. Second, a human at partner A authors a rule per Moment 1 specifying behavior for a class of operations; the rule is substrate-resident at partner A, carries provenance attributing it to its author, and is operationally in force for partner-A operations. Third, a human at partner B authors a rule per Moment 1 specifying different behavior for the same class of operations; that rule is substrate-resident at partner B and operationally in force for partner-B operations. Fourth, the class of operations the rules govern includes situations that span the partners — a cross-partner consultation, a composed view, or any operation whose execution path crosses the boundary; within either partner alone the rules are coherent and operative, while at the boundary between them they disagree. Fifth, neither author has authority within the other partner's governance scope, so the conflict cannot be resolved by either author acting unilaterally without crossing an authority boundary the architecture explicitly preserves.

The disagreement is rule conflict, not data conflict: the question is which rule applies, not which value is correct. What the boundary demands is a treatment architecturally coherent across the partners, not one that quietly violates per-substrate governance to expedite resolution.

## 3. The architectural commitments stressed

Five commitments are stressed in this boundary case.

*Composition requirements.* Per-substrate human governance must be preserved through the conflict; conflict preservation must hold across the partner boundary; cross-boundary path retraceability must remain intact; AI-as-substrate-mediator must hold at every layer; and human-selective composition must continue to govern what gets composed.

*Source-of-truth for rules across partners.* Each partner's substrate is authoritative for which rules apply at that partner. The cross-partner question — which partner's rule applies when the operation spans the partners — is not answerable by reading either partner's substrate alone. The source-of-truth commitment therefore extends to "what cross-partner rules apply" only if substrate content somewhere in the composition records that.

*Authority distribution across partners.* Authority assignments are themselves substrate content, not configuration external to the substrate. Each partner records who has what authority within that partner; cross-partner authority is not present unless explicitly established, and where established is itself substrate content with provenance.

*Conflict-as-first-class extended cross-partner.* Within a single substrate, contradictions are first-class addressable substrate objects, persisted by default and never collapsed by automated processes (§5, §5.3). The cross-partner rule conflict is an instance of this commitment in its composed form: it must be registered, addressable, and resolved only by human-authorized means.

*Rule authoring for resolution.* Resolutions of rule conflicts are themselves rules — substrate-resident, human-authored, paid for at Moment 1. The cross-partner case requires a meta-rule that addresses which rule applies in the cross-partner situation, authored under the same Moment-1 commitment as any other rule, with the additional constraint that the human authoring it must hold authority that spans both partners.

The five commitments are not in tension; the treatment that follows preserves all five simultaneously. What the boundary case reveals is that satisfying them requires an architectural element — cross-partner authority — that does not exist by default and must be explicitly established.

## 4. The architectural treatment

The treatment has four parts.

**(a) Each partner's rule remains substrate-resident authoritative content within that partner.** Neither rule is mutated, overwritten, or downgraded as a consequence of the conflict. The partner-A author retains the rights to inspect, modify, and override the partner-A rule; the partner-B author retains the same rights for the partner-B rule. Resolution does not require either partner to surrender authority over its own substrate; it requires only that the cross-partner question be answered through a separate construct.

**(b) The cross-partner conflict is registered as a first-class substrate object with provenance distinguishing the partners' authors.** The conflict has its own identity, writer attribution (the cell or process that detected it, executing under a rule authorizing detection), timestamp, and explicit relationship to both contradicting rules. The two underlying rules continue to live in their respective partners; the conflict object is substrate-resident in a substrate that participates in the composition and is reachable by humans with cross-partner inspection access. Whether that substrate is one of the two partners, a third "spanning" substrate within the composition, or a substrate dedicated to cross-partner authority is a deployment decision; the architectural requirement is that the conflict object be substrate-resident somewhere in the composition and addressable through cross-partner inspection.

**(c) Resolution requires a meta-rule authored by humans whose authority spans the partners.** The meta-rule is itself substrate-resident, addressable, and traceable, carrying writer attribution, timestamp, rationale, and reference to the conflicting rules it resolves. The authority distribution under which the meta-rule's author has cross-partner authority is itself substrate content, recorded in the composition before the meta-rule it authorizes is written. Four legitimate patterns instantiate cross-partner authority. *Designated cross-partner authority*: the recorded distribution names specific humans as holding authority spanning the partners, and one of them authors the meta-rule. *Collaborative cross-partner authoring*: representatives from each partner, holding combined authority through the recorded distribution, collaboratively author the meta-rule via a within-partner-style conflict-resolution process applied at the cross-partner layer. *Hierarchical authority*: humans at a higher organizational level whose recorded authority encompasses both partners author the meta-rule, with partner-level authors retaining their within-partner authority unaffected. *Federation authority*: the recorded distribution carries federation-level authority for cross-federation conflicts, and a federation-authority human authors the meta-rule. Each pattern is a valid instantiation; what the architecture requires is that the pattern in use be recorded as substrate content before the meta-rule it authorizes can take effect.

**(d) Until cross-partner authority is established and the meta-rule authored, partner-internal rules govern affected operations through fail-defer-default behavior.** The architecture does not allow cross-partner operations affected by an unresolved conflict to proceed under either partner's rule unilaterally, because that would silently elevate one partner's rule to cross-partner status without authorization. Each partner's rules specify the partner-internal response: the operation may fail with a clear error, defer until resolution, or apply a rule-specified default behavior whose scope is explicitly partner-internal. The choice among fail, defer, and default is itself rule content authored within the partner. The graceful degradation is not architecturally automatic; it is architecturally specified, with the specifications living as substrate content in each partner. If no human in the deployment holds cross-partner authority, the architecture cannot resolve the conflict and does not pretend to: the path forward is establishment of cross-partner authority through an authority-distribution change, treated as a governance event in its own right under the authority-distribution-change boundary treatment. The architecture distinguishes "conflict that cannot yet be resolved" — the normal fail-defer-default state pending governance action — from "conflict that the architecture cannot represent," which does not arise here because the conflict is preserved as first-class substrate content regardless of whether resolution authority exists.

## 5. Anti-pattern treatments that violate the architecture

Eight treatments look like resolutions but produce systems that no longer instantiate the CKS commitments.

*Auto-merge cross-partner rules.* Conflicting rules are merged automatically into a synthesized rule that "satisfies both." This is contradiction collapse: the conflict is destroyed rather than resolved, and the synthesized rule has no substrate-resident author with authority over the merge.

*Vendor-managed cross-partner rule precedence.* A vendor system embedded in the composition determines which partner's rule wins, by configuration external to either partner's substrate. This violates source-of-truth (rules are substrate content, not vendor configuration) and authority distribution (authority is substrate content, not vendor policy).

*LLM-mediated cross-partner resolution.* An LLM is given the two rules and asked to produce a resolution. This is the canonical case of an LLM exercising governance authority over rule conflict, which the source paper explicitly excludes (§4.2, §5.3); the LLM is mediator, not authority.

*Primary-partner-rules-win without explicit meta-rule.* The composition treats one partner as the default-authoritative one for cross-partner conflicts, without an explicit meta-rule specifying this. "Which rules apply" must be substrate content, and the authority making this designation must be substrate content; an unwritten default is neither.

*Framework-default precedence.* An integration framework, agent framework, or workflow engine imposes precedence between the partners' rules as part of its own behavior. The architecture does not permit framework-layer precedence over substrate-layer rules; the substrate is authoritative and the framework operates over it, not the inverse.

*Composition-coordinator makes decisions.* An automatic coordinator within the composition resolves the conflict on behalf of the partners. This violates human-governed regardless of how the coordinator was configured: an automatic process that decides which partner's rule applies is exercising governance authority that the substrate-recorded distribution has not assigned to a human.

*First-authored-rule-wins.* The earlier-authored rule is given precedence by temporal order, with no rule specifying this. Temporal precedence is not authorized authority; it is a coincidence of authoring timestamps.

*Compliance-framework overrides partner rules.* A compliance framework imposes cross-partner precedence outside the rule-authoring and authority-distribution architecture. Compliance content is substrate content when it is incorporated into the architecture as rules; a compliance framework operating outside the substrate as an external override violates source-of-truth and human-governed simultaneously.

The eight share a common shape: each resolves the conflict by relocating governance authority from where the architecture places it (substrate-resident, human-authored, recorded distribution) to somewhere the architecture does not. Naming them is what makes the drift visible at the moment a resolution is being chosen.

## 6. Operational implications

Four implications follow directly. *Cross-partner authority must be explicitly established before cross-partner rule conflicts can be resolved architecturally.* Deployments that anticipate cross-partner operations should establish such authority at composition design time, rather than waiting for the first conflict to surface and discovering that no resolution path exists. *Until cross-partner authority is established, the architecture's response is graceful degradation specified by partner-internal rules.* The system does not pretend to resolve what it cannot resolve; the fail-defer-default response is itself a form of governance, with each partner's authors specifying in advance what their substrate does when the composition cannot resolve a cross-partner conflict. *Resolution is a governance event, not an operational one.* When a meta-rule is authored, the authoring is recorded as substrate content, traceable, addressable, and subject to subsequent inspection and override per the human-governed commitment, preserving governance preservation across composition. *Path retraceability is preserved across the resolution.* The trace of any cross-partner operation that proceeds under the meta-rule runs through the meta-rule, the authority distribution that authorized its author, the underlying conflicting rules, and the conflict object that registered the conflict; none of this trail is reconstructed and all of it is substrate-resident.

## 7. Limits of the architectural treatment

The treatment applies to one specific boundary case: rule conflict between rules authored at different composition partners, where the conflict spans the partners' authority boundaries. Adjacent cases have different architectural treatments and are not addressed here. Within-partner rule conflicts are resolved under within-partner authority by the within-partner rule-conflict treatment. Authority distribution conflicts — disputes over who has what authority — are governed by the authority-distribution-change treatment, which is independent of and separately applied from the cross-partner rule-conflict treatment, even when the two surface together in practice. Concurrent writes within a single substrate are conflicts at the data layer, not the rule layer, and are governed by the within-substrate concurrent-write treatment. Partition-induced conflicts arise when the partners are temporarily unable to communicate and operate under their rules independently in the partition; the resulting conflicts are partition-recovery conflicts, not multi-author rule conflicts in the sense of this note. The treatment is also limited to architectural shape: operational details — the specific schema of cross-partner authority records, the wire format of meta-rules, the routing of fail-defer-default responses — are deployment decisions outside the architectural commitment. The architecture specifies what must hold; specific mechanisms are open work consistent with the constraints.

## 8. Operational test

A deployment handles the cross-partner rule authoring conflict boundary in CKS-coherent form if and only if all of the following are true at the moment of conflict and during its persistence:

1. Each partner's rule remains substrate-resident authoritative content within that partner; per-substrate human governance over the rule is preserved.
2. The cross-partner rule conflict is registered as a first-class substrate object with writer attribution, timestamp, rationale, and explicit relationship to both contradicting rules.
3. Resolution, when it occurs, is via a meta-rule authored by a human (or humans) whose authority spans the partners; the authority distribution that grounds that authoring is itself substrate content recorded before the meta-rule takes effect.
4. The legitimate authority pattern in use — designated, collaborative, hierarchical, or federation — is identifiable from substrate content; no implicit cross-partner authority is exercised.
5. Until resolution, cross-partner operations affected by the conflict are governed by partner-internal rules specifying fail, defer, or default behavior; no automatic cross-partner resolution occurs.
6. No vendor system, framework, LLM, default-precedence policy, temporal-order rule, compliance layer, or composition coordinator is permitted to determine which partner's rule applies, in principle or in practice.

A deployment that fails any of (1)–(6) may be operating under some other coherent architecture, but is not handling the boundary case in CKS-coherent form.

## 9. Why naming this boundary as standalone matters

Cross-partner deployments are how CKS substrates appear in real organizations as the substrates aggregate into workflows. Parallel rule authoring is not pathological; it is the default form of rule authoring when each partner is human-governed in its own scope. The boundary case formalized here is therefore not a corner condition but a frequent operational shape of the rule-authoring problem in composed deployments.

The standalone framing serves three purposes. It separates the cross-partner rule-conflict treatment from within-partner conflict treatment, preventing implementers from applying within-partner resolution to a case where no within-partner authority reaches the conflict. It makes the cross-partner-authority requirement visible at composition design time, where it can be planned for, rather than at first-conflict time, where it would surface as a system that cannot proceed. And it forecloses the eight anti-patterns precisely, by name, so that drift toward each is recognizable at the moment a resolution is being chosen rather than retrospectively.

This note is the twelfth of the Phase A6 boundary cases. It follows the within-partner rule-conflict boundary and the substrate concurrent-write race boundary, and extends the rule-conflict treatment to the cross-partner case. Subsequent Phase A6 notes cover AI training-data inclusion, deployment-evolution rule version compatibility, and schema evolution / substrate migration, closing Phase A6 of the Series A derivation program.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cross-Partner Rule Authoring Conflict During Composition: A Boundary Case in the Coordination Knowledge Substrate Pattern.* May 7, 2026. ORCID: 0009-0004-8065-3235.
