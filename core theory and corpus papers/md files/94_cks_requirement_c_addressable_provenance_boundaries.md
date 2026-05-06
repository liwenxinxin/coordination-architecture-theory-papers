# References as Substrate Content: Requirement C of CKS Composition and the Preservation of Path Retraceability Across Composing Systems

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 5, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, Requirement C of the CKS composition specification — that cross-boundary references between composing systems are substrate content with substrate-resident addressable identifiers — as a standalone architectural commitment that can be defended, implemented, and tested independently of the other four composition requirements and the broader composition framework.

## Abstract

The CKS composition specification (Li, April 2026, §13.3; formalized at the integrating level in the composition-requirements parent note) names five requirements that any multi-substrate composition must satisfy to remain CKS-coherent. Requirement C — addressable provenance across boundaries — extends the path-retraceability commitment (Claim 1, §3.1) across composition boundaries by requiring that cross-boundary references be substrate content with substrate-resident addressable identifiers, not external tracking metadata. The requirement is operationally distinct from external cross-system tracking patterns commonly conflated with it: audit logs spanning systems, distributed tracing infrastructure, message-queue correlation, and federated provenance. This note articulates the four operational components of Requirement C, distinguishes it from the four adjacent patterns, names ten failure modes, and provides an operational test for whether a composition's cross-boundary addressability satisfies the requirement.

## 1. Why Requirement C needs to be formalized as standalone

The parent foundational note commits to five composition requirements. The integrating-frame note named Requirement C at the integrating level. The two prior specializations have formalized Requirement A (per-substrate human governance) and Requirement B (conflict preservation across boundaries). This note formalizes Requirement C, with particular weight on the commitment that cross-boundary references must be substrate content rather than external tracking metadata.

The motivating cases are deployments where CKS substrates compose with other systems and where cross-boundary paths must be reconstructible: a CKS substrate composing with a CKS substrate from another team, where coordination decisions span team boundaries; a CKS substrate composing with an enterprise system, where decisions in the substrate were informed by enterprise-system data; multiple CKS substrates composing in cascade, where decisions in one substrate inform decisions in another. Each case requires path reconstruction across the boundary, which requires Requirement C — cross-boundary references as substrate-addressable content.

A second motivation is the strategic prior-art posture. Requirement C is consequential prior art because it forecloses composition architectures that externalize cross-boundary tracking. Patentable derivations focused on cross-system AI architectures with retraceability, multi-substrate AI architectures with substrate-only paths, or hybrid AI systems with cross-boundary provenance are substantially more defensibly contested when Requirement C is publicly formalized as standalone.

A third motivation is the connection to the within-substrate commitments Requirement C extends. Path retraceability commits to paths being reconstructible from substrate content; Guarantee C of the determinism contract commits to within-substrate changes being addressable. Requirement C extends both across composition boundaries.

## 2. The Requirement C commitment, defined precisely

The architectural commitment has four operational components.

**(a) Cross-boundary references as substrate content.** When CKS substrate S1 composes with system S2 and S1 contains content that originates from or relates to content in S2, the cross-boundary reference is itself substrate content within S1. The reference is not an external audit-log entry, not a distributed-tracing trace ID held in tracing infrastructure, not a message-queue correlation ID held in queue metadata. It persists with S1's other content and is governed by the same substrate-layer commitments.

**(b) Substrate-resident addressable identifiers.** Each cross-boundary reference has an identifier assigned within S1's substrate that permits the reference to be queried, traced, and navigated through standard substrate read operations. The identifier is substrate-assigned, not external-system-assigned. The distinction between (a) and (b) is operationally meaningful: (a) names what the reference is — substrate content — and (b) names the addressing scheme — that the substrate, not an external system, is the source of the addresses. A composition can satisfy (a) while failing (b) if substrate content carries cross-boundary references whose only durable identifiers are external.

**(c) Cross-boundary provenance fields.** The cross-boundary reference carries the six provenance fields specified in the path-retraceability decomposition — writer attribution (the cross-boundary actor or rule), timestamp (when the cross-boundary content was incorporated into S1), antecedent reference (the content in S2 that S1 references), rule reference (if a rule mediated the cross-boundary connection per one of the three hybrid-systems composition patterns), rationale where applicable, and relationship metadata identifying the kind of cross-boundary relationship — input from S2 (Pattern A), derivation of S2 (Pattern B), or separate concern (Pattern C). All six fields are substrate-resident and addressable through (b).

**(d) Substrate-only paths across boundaries.** Substrate-only paths extend across composition boundaries because cross-boundary references are substrate content. A path reconstructed from S1's substrate may include cross-boundary references that point to content in S2; the references are substrate-resident within S1, so the path traversal from S1's perspective remains substrate-only. If S2 is also CKS, S2's substrate-only paths compose with S1's. If S2 is non-CKS, S1's substrate-only paths terminate at the cross-boundary references, with the references identifying where the path crosses the boundary and substrate-only paths preserved up to that point.

The four components together define Requirement C architecturally. A composition that satisfies all four has Requirement C in the architectural sense; a composition that fails any one does not, regardless of whether cross-boundary tracking functions operationally through external mechanisms.

## 3. What Requirement C does not claim

Six limitations bound the commitment so that the standalone treatment is not overstated.

**Not all content references S2.** Requirement C does not claim that all content in S1 must reference content in S2. Most content in S1 is purely within-S1; Requirement C applies to content with a cross-boundary relationship.

**Not a CKS-on-both-sides requirement.** Requirement C does not require composing systems to themselves have CKS-style addressability. Compositions with non-CKS systems are architecturally supported under the hybrid-systems composition framework. The architectural commitment is that the CKS substrate has addressable cross-boundary references; the composing system may have any internal addressability model, or none.

**Not a foreclosure of external tracking.** Requirement C does not foreclose external cross-system tracking infrastructure. Deployments may have audit logs, distributed tracing, or other tracking systems; the architectural commitment is that the substrate has its own addressable cross-boundary references regardless. External tracking may exist as a derivative view of substrate content under Pattern B of the hybrid-systems framework.

**Not an implementation specification.** Requirement C does not specify implementation patterns. Implementations may use foreign-key-style references, URI-based references, substrate-resident proxy entities, or other mechanisms; the architectural commitment is to the four components being operationally satisfied. Specific mechanisms are deployment choices.

**Not a global-uniqueness requirement.** Requirement C does not require cross-boundary references to be globally unique across all composing systems. The references are addressable within S1's substrate; their global uniqueness may be operationally relevant for specific deployment patterns but is not architecturally required.

**Not an unconditional-visibility requirement.** Requirement C does not require cross-boundary references to be visible to all readers. Visibility may be authority-scoped under the read-authority decomposition; the architectural commitment is that cross-boundary references are substrate content with addressability, not that they are universally visible.

## 4. What Requirement C is not

Four adjacent cross-system tracking patterns are commonly conflated with Requirement C. Distinguishing each clarifies the standalone commitment.

**Not audit logs spanning systems.** Audit-log infrastructure that spans composing systems records cross-system operations in centralized logs external to substrate. Requirement C is different: cross-boundary references are substrate content within the CKS substrate. A composition with comprehensive audit logging may still violate Requirement C if cross-boundary references are not themselves substrate content.

**Not distributed tracing infrastructure.** Distributed tracing systems trace requests across services with trace IDs and span data held in tracing infrastructure. Requirement C is different: cross-boundary references are substrate content with substrate-resident identifiers. Distributed tracing addresses operational tracing of requests; Requirement C addresses architectural addressability of cross-boundary content. The two operate on different layers and can coexist.

**Not message-queue correlation IDs.** Message-queue infrastructure uses correlation IDs to track related messages across asynchronous flows. The correlation IDs are queue-infrastructure metadata. Requirement C is different: cross-boundary references are substrate-resident content. A composition may use message queues for cross-system communication while satisfying Requirement C, provided the resulting substrate content preserves cross-boundary references with substrate-addressable identifiers.

**Not federated provenance systems.** Federated provenance systems distribute provenance metadata across federated services. Requirement C is different: provenance for cross-boundary references is substrate-resident within the CKS substrate, not in federated infrastructure.

In each case the adjacent pattern is a real and useful infrastructure concern; none is a substitute for Requirement C, and a deployment that satisfies any of them while failing the substrate-residence commitment does not satisfy the requirement.

## 5. Why Requirement C is load-bearing

Requirement C is load-bearing for several CKS commitments.

It is load-bearing for the integrating composition-requirements specification: Requirement C is one of the five requirements, and without cross-boundary addressability, paths that span compositions cannot be reconstructed.

It is load-bearing for path retraceability and the path-retraceability decomposition. The foundational commitment specifies reconstructible paths within a substrate; Requirement C extends the commitment across composition boundaries. Without Requirement C, path retraceability would hold only within single substrates, and substrate-only paths could not extend across compositions because cross-boundary references would not be substrate-resident.

It is load-bearing for Guarantee C of the determinism contract. The guarantee specifies addressability within a substrate; Requirement C specifies the parallel addressability across compositions. The two together give addressability of the whole — within and across.

It is load-bearing for Requirement B of the composition specification. Requirement B's preservation of cross-substrate conflict relationships depends on those relationships being addressable substrate content; Requirement C provides the addressability. The two requirements compose: Requirement B specifies that cross-boundary conflict relationships are preserved as first-class addressable objects; Requirement C specifies that the cross-boundary references those relationships rely on are substrate-resident and addressable.

It is load-bearing for the accountability-question answers. The four accountability questions — what was decided, by whom, under what authority, with what rationale — may have answers that span composition boundaries; Requirement C ensures the cross-boundary references answering those questions are substrate-resident.

## 6. Failure modes that violate Requirement C

Each failure mode names a way an implementation can fail by externalizing cross-boundary references or compromising their addressability.

**(a) External cross-boundary tracking only.** Cross-boundary references are tracked in external systems — audit logs, tracing infrastructure, queue metadata — without substrate-resident references. Component (a) of §2 fails: the references are not substrate content.

**(b) Cross-boundary references as opaque pointers.** Substrate-resident references exist but are opaque pointers to external systems without the provenance fields. Component (c) fails: the references are not operationally useful for path reconstruction.

**(c) External-identifier-only addressability.** Cross-boundary references are assigned identifiers from external systems and are addressable only through those external systems, not through the substrate's own scheme. Component (b) fails: the addressing scheme is not substrate-resident.

**(d) Cross-boundary-reference stripping during composition.** When content is incorporated from a composing system, the cross-boundary references are stripped, and the incorporated content is treated as if native to the CKS substrate. Component (d) fails: there is no record of cross-boundary origin, and substrate-only paths cannot reach back across the boundary.

**(e) Cross-boundary-provenance stripping.** Cross-boundary references are recorded but the provenance fields are stripped. The references identify cross-boundary relationships but lack the writer attribution, timestamp, antecedent, rule reference, or rationale that make them operationally useful for path retraceability.

**(f) Cross-boundary-reference archival to external storage.** Recent cross-boundary references persist in substrate; older references are archived to external systems. Substrate-resident addressability holds only for recent references and degrades over time.

**(g) Implicit cross-boundary references.** Content flows from S2 into S1 without any explicit cross-boundary reference being created in S1's substrate. The references do not exist as substrate content, so cross-boundary path reconstruction is impossible from within S1.

**(h) Cross-boundary-reference summarization.** Cross-boundary references are periodically summarized into aggregate statistics or compressed representations that lose the individual reference identifiers and provenance. After summarization, individual cross-boundary references are no longer addressable.

**(i) Composition-boundary-bypass paths.** Alternative cross-boundary content flows exist that bypass the substrate-resident reference architecture — direct API calls from S1 to S2 that incorporate content without producing substrate-resident references. The commitment that all cross-boundary content produces addressable substrate references fails for the bypass paths, even when a parallel reference architecture exists for non-bypass flows.

**(j) Federated provenance without substrate anchoring.** Cross-boundary provenance is maintained in federated provenance systems without substrate-anchored references. Cross-boundary path reconstruction requires federated-system queries rather than substrate reads; substrate-only paths across boundaries fails.

A composition that exhibits any of (a)–(j) does not satisfy Requirement C, regardless of whether cross-boundary tracking functions through external infrastructure.

## 7. Operational test

A composition satisfies Requirement C if and only if all of the following are true at all times during the composition's existence.

1. Cross-boundary references are substrate content within each composing CKS substrate, per component (a) of §2.

2. Cross-boundary references have substrate-resident addressable identifiers, per component (b) of §2.

3. Cross-boundary references carry the six provenance fields specified in the path-retraceability decomposition, per component (c) of §2.

4. Substrate-only paths extend across composition boundaries through cross-boundary references, per component (d) of §2.

5. Cross-boundary references are queryable through standard substrate read operations.

6. No alternative cross-boundary content flows exist that bypass the substrate-resident reference architecture; all cross-boundary content produces addressable substrate references.

A composition that fails any of (1)–(6) does not satisfy Requirement C, even if cross-boundary tracking functions through external mechanisms.

## 8. Conclusion

Implementations under pressure to integrate AI systems with enterprise infrastructure consistently drift toward external cross-boundary tracking patterns that violate Requirement C. The drift is steady because external tracking infrastructure — audit logs, distributed tracing, message-queue correlation, federated provenance — is operationally established for cross-system tracking, and replicating its functionality as substrate-resident references can appear redundant when external infrastructure already tracks cross-system flows.

The drift produces systems where cross-boundary tracking is external while the substrate carries the cross-boundary content. The downstream consequences manifest as path-retraceability failures across compositions, Requirement B failures (cross-boundary conflict relationships cannot be addressed because the references they rely on are external), accountability failures (the four accountability questions cannot be answered from substrate alone), and source-of-truth fragmentation (cross-boundary tracking becomes external while substrate is authoritative for the local content, splitting authority across systems).

Naming Requirement C as a standalone architectural commitment — with the four operational components, the six limitations, the four adjacent-pattern distinctions, the load-bearing connections, the ten failure modes, and the operational test — gives downstream readers a precise specification of the cross-boundary addressability the architecture requires. Subsequent specializations treat Requirement D (AI-as-substrate-mediator at every layer) and Requirement E (human-selective composition).

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *References as Substrate Content: Requirement C of CKS Composition and the Preservation of Path Retraceability Across Composing Systems.* May 5, 2026. ORCID: 0009-0004-8065-3235.
