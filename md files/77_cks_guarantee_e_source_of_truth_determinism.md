# Source-of-Truth Determinism: Guarantee E of the CKS Determinism Contract as a Standalone Architectural Commitment

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the fifth guarantee of the CKS determinism contract — that the substrate is the source of truth for the contract's properties — as a standalone architectural commitment, with a four-component definition, a set of clarifications about what the commitment does not claim, distinctions from adjacent patterns commonly conflated with it, named failure modes, and an operational test.

## Abstract

The CKS determinism contract introduced in §4.1 of the source paper and formalized in derivation note A1.10 makes five guarantees about substrate behavior. The integrating-frame note A2.55 enumerated the five at the contract level; A2.56 formalized the substrate-vs-model-output boundary that scopes the contract; A2.57–A2.60 formalized the first four guarantees as standalone commitments. This note formalizes the fifth: Guarantee E, that substrate is the source of truth for the determinism properties Guarantees A–D specify. Guarantee E is the binding guarantee that anchors the prior four to substrate. Without it, Guarantees A–D can be satisfied substrate-internally while the contract as a whole is compromised at the substrate boundary by external systems' authority claims for the same properties. The note states the four-component definition of Guarantee E (substrate-internal contract; external-system non-overriding; source-of-truth maintenance across the determinism properties; substrate-only-paths preservation), distinguishes it from adjacent commitments (the broader source-of-truth commitment per A1.08, the source-of-truth-vs-mirror-of-truth distinction per A2.48, eventual consistency with read repair, and global-state authority), names ten failure modes, and provides an operational test.

## 1. Why Guarantee E needs to be formalized as standalone

The motivating concern is a failure mode the integrating frame for the determinism contract leaves implicit. Guarantees A–D are individually satisfiable while the contract as a whole is not: a system can exhibit representation determinism, cell-behavior determinism, change addressability, and conflict preservation within its substrate while resolving disagreements between substrate and adjacent components in favor of the adjacent components. What reads return then depends on whether read-repair has fired against an external authoritative source; whether cells behave equivalently depends on whether external systems are currently consistent with substrate. The four guarantees hold substrate-internally, but the contract is not, in any defensible sense, a contract about *substrate*. Guarantee E names this failure mode and forecloses it.

A second motivation is the prior-art posture. Architectures positioning external systems — databases, audit infrastructures, distributed-consensus systems, identity providers — as authoritative for specific determinism properties of substrate are common in enterprise integration, where deferring to an established authoritative system reduces apparent integration friction. A standalone treatment of Guarantee E places the substrate-internal-contract architecture in the public prior art, foreclosing claims that external-authority-driven determinism in coordination substrates is a novel invention rather than a contested design choice.

A third motivation is the relationship to the broader source-of-truth commitments. A1.08 commits to substrate being authoritative for the five categories of coordination state (decisions, by-whom, authority, rationale, conflicts). A2.48 specifies the architectural distinction between source-of-truth (substrate is the source from which derivative views flow) and mirror-of-truth (substrate is a derivative view of authority held elsewhere). The three commitments compose: A1.08 establishes that substrate is authoritative for coordination state; A2.48 specifies that the authority is architectural rather than derivative; Guarantee E specifies that the contract — the statement of what substrate guarantees about its own determinism behavior — is itself substrate-internal, unweakened by external systems' authority claims for the same properties. A2.61 articulates Guarantee E as the determinism-level specialization within this structure.

## 2. The Guarantee E commitment, defined precisely

Guarantee E is the architectural commitment that the determinism contract A1.10 operates substrate-internally and that substrate is authoritative for the determinism properties Guarantees A–D specify. The commitment decomposes into four operational components.

**(a) Substrate-internal contract.** The determinism contract operates within substrate. Guarantees A–D are commitments about substrate's own representation, persistence, read behavior, change addressability, and conflict preservation. The contract is not a system-wide commitment shared with adjacent components; it is substrate-bounded. Adjacent components per Pattern B of A1.16 may have their own determinism properties, but the contract A1.10 specifies properties of substrate, not properties shared with the surrounding system.

**(b) External-system non-overriding.** External systems do not override substrate's determinism properties. When substrate and an external system disagree on content, current state, decisions, conflicts, orchestration rules, or authority assignments — the five categories per A2.42–A2.47 — substrate prevails per A1.08. Whatever determinism properties external systems have for their own state, those properties do not propagate into substrate as authority. External non-determinism, eventual consistency, or asserted authority over the same fact is non-authoritative when substrate is the source.

**(c) Source-of-truth maintenance across the determinism properties.** For each property Guarantees A–D specify — read content (Guarantee A), cell behavior given identical inputs (Guarantee B), change addressability (Guarantee C), conflict preservation (Guarantee D) — substrate is the source from which the property derives. Derivative views may have their own determinism properties, or may be eventually consistent, or may be non-deterministic in their own right. None of these affect substrate's. The four guarantees are guarantees about substrate, terminable at substrate.

**(d) Substrate-only-paths preservation.** Paths through the determinism properties — substrate-only paths per A2.41 — remain substrate-only. Path traversal does not require consulting external systems for any element the contract covers. The four accountability questions per A2.36–A2.39, the six provenance fields per A2.40, the change addressability per Guarantee C, and the conflict-preservation guarantees per Guarantee D are all substrate-resident and substrate-authoritative.

The four components together define Guarantee E architecturally. A system that satisfies all four has source-of-truth determinism in the architectural sense.

## 3. What the guarantee does NOT claim

Six clarifications, to prevent the standalone treatment from being read as more demanding than it is.

**(a) Not external-system absence.** Deployments may have rich external derivative views, adjacent AI components, and integration systems per A1.16. The architectural commitment is to the determinism contract operating substrate-internally, not to external-system absence.

**(b) Not symmetric determinism.** Adjacent components per Pattern B of A1.16 may be eventually consistent, non-deterministic, or have other operational properties that differ from substrate's. Guarantee E does not require the surrounding system to satisfy similar properties; it specifies substrate's own determinism contract.

**(c) Not closure to human-driven external knowledge.** Humans exercising the modify and override rights per A2.02 and A2.03 may revise substrate based on knowledge from external sources. The revisions become substrate content per the boundary-crossing pattern A2.10, with substrate's determinism properties holding for the revised state. Guarantee E does not foreclose informing substrate from outside; it specifies that, once content is in substrate, the contract's properties are substrate's.

**(d) Not implementation specificity.** Implementations may use various mechanisms — substrate-first writes, downstream propagation to derivative views, conflict resolution in favor of substrate at the integration boundary, scheduled reconciliation. The architectural commitment is to the four components being operationally satisfied; specific mechanisms are deployment choices.

**(e) Not unobservability to external systems.** External systems may query substrate via standard read operations per A2.25 Requirement 2, or via derivative views downstream of substrate; the contract's properties hold for substrate's reads regardless. Guarantee E specifies substrate is the source, not that substrate must be invisible.

**(f) Not foreclosure of migration.** Migration safety per A1.05 commits to substrate moving between hosts while preserving architectural commitments. Guarantee E is preserved across migration provided the new host satisfies the three minimal requirements per A2.24–A2.26 and the migration itself does not externalize the contract's properties to host infrastructure that does not migrate with substrate. §6(j) names the implementation pathway under which this could fail.

## 4. What the guarantee is NOT: adjacent patterns commonly conflated with it

Four distinctions sharpen what Guarantee E adds beyond commitments it is sometimes read as duplicating.

**Not the broader source-of-truth commitment per A1.08.** A1.08 commits to substrate being authoritative for the five categories of coordination state (decisions, by-whom, authority, rationale, conflicts) — a commitment about *which state* is treated as authoritative for coordination questions. Guarantee E is a commitment about *which determinism properties* are substrate's. A system can satisfy A1.08 (substrate is authoritative for the five categories) while failing Guarantee E (the determinism properties Guarantees A–D specify are compromised by external interactions). Guarantee E is the determinism-level specialization within A1.08's broader source-of-truth posture.

**Not the source-of-truth-vs-mirror-of-truth distinction per A2.48.** A2.48 specifies the architectural distinction between source-of-truth (substrate is the source from which derivative views flow) and mirror-of-truth (substrate is a derivative view of authoritative state held elsewhere). The distinction is positional: where the architectural source sits. Guarantee E operates within the source-of-truth posture, articulating the determinism-level commitments that posture entails for the contract A1.10.

**Not eventual consistency with read repair.** Eventual-consistency architectures with read repair produce reads that *eventually* satisfy consistency properties, with read-repair mechanisms updating local content based on external authoritative state. Guarantee E forbids this when read repair compromises substrate's determinism: substrate's content is not updated based on an external system's authority claim. Eventual consistency is admissible *between* substrate and its derivative views — substrate is the convergence target — but not *into* substrate from external authority.

**Not global-state authority.** Global-state architectures position a single authoritative state across the entire system, with all components consulting that state. Guarantee E is different: substrate is locally authoritative for the determinism contract, with the contract bounded to substrate. Other components may have their own state, authority, and determinism properties; the contract A1.10 does not extend across them.

## 5. Why Guarantee E is load-bearing for downstream commitments

Guarantee E supports several CKS commitments. The dependencies are direct enough that a system failing Guarantee E fails or weakens these commitments in ways the integrating frames do not catch.

The integrating contract A1.10 binds to substrate through Guarantee E. Without it, A1.10 can be partially satisfied (Guarantees A–D substrate-internally) while the contract as a whole is compromised at the substrate boundary.

Each of Guarantees A–D, A2.57–A2.60, depends on Guarantee E for its substrate scope. Each prior guarantee commits to a specific determinism property; Guarantee E anchors all four to substrate. A system that satisfies A only when external systems are operational, or D only when external authority is consistent with substrate, satisfies A and D in name but not as substrate properties.

The broader source-of-truth commitment A1.08 composes with Guarantee E. A1.08 establishes substrate authority for the five categories of coordination state; Guarantee E ensures the determinism contract is itself maintained within that authority. Failing Guarantee E weakens A1.08's authority claim by making it conditional on external systems for the contract's properties.

The source-of-truth-vs-mirror-of-truth distinction A2.48 is the architectural posture within which Guarantee E operates. Where A2.48 specifies that substrate is the architectural source, Guarantee E specifies that the determinism contract operates within that source. A system in a mirror-of-truth posture with respect to external authority cannot satisfy Guarantee E.

The substrate-only-paths property A2.41 requires all path elements to be substrate-resident. Guarantee E ensures the determinism properties supporting path traversal are themselves substrate-internal. Without it, paths could traverse external systems for authoritative determinism content, breaking A2.41.

Migration safety A1.05 moves substrate between hosts while preserving architectural commitments. Guarantee E ensures the contract moves with substrate, not with external infrastructure. A contract that depends on external authority for its properties is not migration-coherent.

## 6. Failure modes that violate the guarantee

Each anti-pattern names a specific way an implementation can fail Guarantee E. The list is enumerative; it does not claim to exhaust the failure surface.

**(a) External-authoritative read repair.** Substrate is operated in eventually-consistent integration with an external authoritative source, with read-repair mechanisms updating substrate content based on external state. Guarantee A's read-determinism becomes a property of the integration, not of substrate.

**(b) Bidirectional sync without substrate primacy.** Substrate and external systems are synchronized bidirectionally, with conflicts resolved by latest-write timestamp or by external-system rules. Component (b) of §2 fails.

**(c) External-write-on-failure fallback.** Substrate is treated as authoritative under normal conditions, but writes fall through to external systems when substrate is unavailable, with later propagation back to substrate when it returns. The fallback path makes external systems authoritative during the failure window.

**(d) External-system-primary determinism.** External systems are positioned as authoritative for specific determinism properties — for example, an external timestamp service authoritative for change-addressability ordering, or an external decision-log service authoritative for accountability traces. Substrate's determinism properties become contingent on external systems for those specific properties.

**(e) Per-category mixed source.** Substrate is positioned as source for some determinism properties (read determinism, conflict preservation) but external systems as source for others (change authority delegated to external audit logs, authority assignments delegated to external identity systems). Component (a) of §2 fails for the externally-sourced properties.

**(f) Eventually-consistent substrate without primacy.** Substrate is operated in distributed-systems eventual consistency without substrate primacy at read time. Reads may return content not yet converged to substrate's authoritative state; the determinism properties hold only after convergence rather than continuously.

**(g) External-derivative override.** External derivative views per Pattern B of A1.16 are permitted to override substrate when they disagree — for performance optimization, or for "consistency" with downstream systems whose state has diverged from substrate. The architectural authority of substrate over its derivative views fails.

**(h) Documentation–operation divergence.** Documentation describes substrate as the source-of-truth for the determinism contract while operational practice resolves disagreements in favor of external systems. The architectural claim and the implemented behavior diverge; the claim is empty.

**(i) External-system-determinism dependence.** Substrate's determinism properties depend on external systems being operational and consistent. When external systems are unavailable or inconsistent, substrate's determinism is degraded. Guarantee E requires substrate's determinism to be substrate-internal, not externally dependent for the properties A–D specify.

**(j) Migration without contract preservation.** Substrate is migrated to a new host but the contract is not preserved on the new host because external infrastructure that supported the contract's properties on the original host is not migrated with substrate. The failure here is implementation rather than architectural, but the implementation failure produces an architectural one.

## 7. Operational test

A system satisfies Guarantee E if and only if all of the following hold continuously throughout substrate's existence.

1. The determinism contract Guarantees A–D specify operates within substrate; the contract's properties are substrate's properties, not properties shared with or derived from external systems (component (a) of §2).

2. When substrate and external systems disagree on any element within the five categories per A2.42–A2.47, substrate prevails per A1.08; external systems do not override substrate's determinism properties (component (b) of §2).

3. For each determinism property Guarantees A–D specify, substrate is the source from which the property derives; derivative views may have their own properties, but substrate's are not contingent on theirs (component (c) of §2).

4. Substrate-only paths per A2.41 remain substrate-only; path traversal across the four accountability questions per A2.36–A2.39, the six provenance fields per A2.40, and the change-addressability and conflict-preservation properties per Guarantees C and D does not require consulting external systems for authority (component (d) of §2).

5. The contract is preserved under failure conditions: substrate's determinism does not depend on external systems being operational or consistent.

6. The contract is preserved under migration per A1.05: substrate moved to a new host preserves the contract on the new host without dependence on external infrastructure that did not migrate with substrate.

A system that fails any of (1)–(6) does not satisfy Guarantee E architecturally, regardless of how it presents source-of-truth properties under typical operating conditions.

## Conclusion

Implementations under pressure to integrate with established enterprise infrastructure consistently drift toward external-system-driven determinism patterns. The drift is steady because external systems — databases, audit infrastructures, distributed-consensus systems, identity providers — are operationally established for various determinism-related purposes, and subordinating substrate's determinism to those systems appears to reduce integration cost. The cost the substitution imposes — that substrate is no longer the source for the determinism properties A1.10 names — is invisible until a failure scenario, a migration, or an external-system inconsistency surfaces it. Determinism-contract failures, source-of-truth fragmentation per A1.08, substrate-only-paths failures per A2.41, and migration-coherence failures per A1.05 are the typical downstream consequences.

Naming Guarantee E as a standalone architectural commitment — with the four operational components in §2, the clarifications in §3, the adjacent-pattern distinctions in §4, the load-bearing connections in §5, the failure modes in §6, and the operational test in §7 — makes the commitment defensible, implementable, and testable independently of its companions. Together with A2.55–A2.60 already drafted and A2.62–A2.63 to follow, the substrate side of A1.10 will be fully formalized: the integrating frame, the substrate/model boundary, and the five guarantees specify substrate's determinism architecture as a coherent contract anchored substrate-internally.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Source-of-Truth Determinism: Guarantee E of the CKS Determinism Contract as a Standalone Architectural Commitment.* CKS Derivation Note A2.61. May 5, 2026. ORCID: 0009-0004-8065-3235.
