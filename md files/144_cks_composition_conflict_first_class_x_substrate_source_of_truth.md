# Substrate-Resident Conflict Structure: The Composition of Conflict-as-First-Class and Substrate-as-Source-of-Truth in the Coordination Knowledge Substrate Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 6, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the Coordination Knowledge Substrate (CKS) pattern introduced in *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the emergent architectural property that arises when two foundational commitments compose — A1.03 (conflict as first-class) and A1.08 (substrate as source of truth) — so that downstream work can adopt or argue against the composition without ambiguity.

## Abstract

The CKS pattern's foundational commitments do not stand alone in operation; they compose, and several composition pairs produce architectural properties that neither commitment yields by itself. This note formalizes the composition of A1.03 (conflict as first-class) and A1.08 (substrate as source of truth). A1.03 alone is satisfied by deployments that preserve contradictions through cell-mediated resolution but treat them as metadata or hold them in non-substrate systems; A1.08 alone is satisfied by deployments that make substrate authoritative for the four non-conflict categories of coordination state while treating conflicts as exceptions. The composition forces contradictions to be authoritative substrate content per A2.45 (Category 3: substrate authoritative for "what is in conflict") — first-class content within the source of truth, not metadata about it. The emergent architectural property is *substrate-resident conflict structure*: contradictions are part of the authoritative state the substrate carries, addressable, governable, and rule-mediated in the same architectural sense as content for the other four source-of-truth categories. This note states the property in four operational components, identifies the architectural decisions the composition forces beyond either commitment alone, distinguishes anti-patterns that violate the composition specifically, contrasts the composition with adjacent patterns commonly conflated with it, and provides an operational test for whether a deployment satisfies it.

## 1. Why the A1.03 × A1.08 composition needs to be formalized as standalone

A1.03 and A1.08 are individually defended commitments in the source paper — A1.03 in §3.2 and §5 (conflict as first-class object with two-level handling) and A1.08 in §11.3 (substrate as source of truth across five categories). Each has a separate decomposition (A2.13–A2.17 for A1.03; A2.42–A2.48 for A1.08) and separate anti-pattern coverage in Phase A3.

The composition is not a corollary of the two decompositions read together. A1.03 alone is operationally satisfiable by architectures where contradictions are preserved per A2.13, recorded as substrate-resident artifacts per A2.17, and resolved at cell scope per A2.14 — *and yet* held as metadata, exception logs, or debug artifacts that are not authoritative for any source-of-truth category. The conflict-handling architecture is in place, but the contradictions occupy the architectural status of side information about substrate state rather than substrate state itself. A1.08 alone is operationally satisfiable by architectures where substrate is authoritative for what was decided (A2.43), what is current (A2.44), what rules apply (A2.46), and who has what authority (A2.47), while leaving "what is in conflict" (A2.45) to be inferred at runtime from external systems, vendor APIs, or implementation logic. The substrate is authoritative, but its authority does not extend to disagreement.

The composition closes the gap. It specifically operationalizes A2.45 through A2.17 — the contradiction edge is not just substrate-resident, it is authoritative substrate content for "what is in conflict." Conflicts join the source of truth. The architectural property the composition produces is substrate-resident conflict structure, and it is what makes CKS architecturally distinctive in conflict-handling among 2024–2026 distributed AI systems where conflicts are commonly treated as errors to be auto-resolved (CRDT primitives, last-write-wins policies), exceptions to be logged outside substrate, edge cases to be handled by ad-hoc mechanisms, or metadata about state inconsistency.

The strategic case for formalizing the composition as standalone is that conflict-handling in distributed AI systems is a dominant 2024–2026 technical concern. Patentable derivations addressing multi-source disagreement handling, AI mediation of contradictions, conflict-as-state architectures, or "consensus-as-state" systems are substantially more defensibly contested when the composition is publicly formalized as prior art. The note also completes, with its sibling A4.07 (A1.03 × A1.07, conflict-provenance), the coverage of how A1.03 composes with the two foundational commitments most directly relevant to its operation: A1.07 (retraceability — *what happened* to a conflict) and A1.08 (source of truth — *what authoritatively is* in conflict). Without publishing the composition as standalone, the conflict-as-authoritative-content property is implicit in the foundational commitments rather than architecturally specified.

## 2. The emergent architectural property, defined precisely

A deployment exhibits substrate-resident conflict structure when all four of the following operational components hold.

**(a) Contradictions are authoritative substrate content addressing A2.45.** Contradiction edges per A2.17 are not artifacts that happen to live in the substrate; they are authoritative substrate content for "what is in conflict" per A2.45. They have the same architectural status as content for the other four source-of-truth categories: A2.43 (what was decided), A2.44 (what is current), A2.46 (what rules apply), and A2.47 (who has what authority). When a coordination question concerns disagreement, the substrate answers; nothing else does.

**(b) "What is in conflict" has architectural specification through contradiction edges.** A2.45 commits to substrate being authoritative for conflict state; the composition operationalizes that commitment through the specific architectural mechanism of the contradiction edge per A2.17. The deployment specifies architecturally what counts as a conflict, how a conflict is represented, where contradiction edges live in the substrate schema, and how they are addressable. Authority over "what is in conflict" without an architectural mechanism for representing it is not satisfied; the composition forces the mechanism into the architecture.

**(c) Conflict-resolution rules are authoritative content governing conflict-handling.** Rules that determine how conflicts per A2.45 are resolved through cell-mediated resolution per A2.14 are themselves authoritative substrate content per A2.46. They are not implementation defaults, vendor configurations, or framework policies. The conflict-handling architecture operates *under* authoritative rules, and the rules are part of the same source of truth as the conflicts they govern.

**(d) Humans govern conflict structure through governance-against-authority applied to A2.45.** The four governance rights per A2.01–A2.04 — inspect, modify, override, rule-author — apply to conflict structure in the same way they apply to other authoritative substrate content. Humans inspect contradictions, modify conflict structure when warranted, override resolution decisions, and author the rules per A2.46 that govern resolution. The A4.01 composition (governance-against-authority) operates on conflict structure because A1.08's authoritative status reaches A2.45.

The four components together define the property architecturally. A deployment satisfying the composition exhibits all four; a deployment failing any one fails the composition.

## 3. What the composition forces beyond either commitment in isolation

A1.03 alone forces conflict preservation, contradiction edges as substrate-resident artifacts, and cell-mediated resolution under rules. A1.08 alone forces substrate to be authoritative for coordination state across five categories. The composition forces eight additional architectural decisions that neither commitment forces individually.

First, contradictions must be authoritative, not metadata. A1.03's preservation requirement per A2.13 is satisfied by storing contradictions; the composition forces them to occupy authoritative status. Contradictions tagged as warning flags, exception logs, anomaly markers, or debug artifacts fail the composition even when preservation per A2.13 is technically met.

Second, A2.45 must be architecturally operationalized. A1.08-alone could be satisfied by substrate being authoritative for the four non-conflict categories with conflicts handled outside the source of truth; the composition forces A2.45's authority into the architecture rather than allowing it to remain a stated commitment without an architectural mechanism.

Third, contradiction edges must be addressable. Stable addresses for contradictions per A2.59 are required so that conflict-related provenance (per A4.07) and reproducibility (per A4.06) can operate over them as authoritative content.

Fourth, conflict-resolution rules must be authoritative content per A2.46 — not hardcoded logic, vendor configuration, or external policies. Resolution that proceeds under non-authoritative rules fails the composition because the resolution does not derive from the source of truth.

Fifth, humans must be able to govern conflict structure through inspect, modify, override, and rule-author rights per A2.01–A2.04. Conflict structure that is held authoritatively but not exposed to governance fails the composition because A1.08's authority is severed from A1.01's governance affordance at A2.45 specifically.

Sixth, conflict structure must persist in substrate across deployment lifecycle. Conflicts that exist only as session-local state, transient runtime artifacts, or deployment-version-specific markers fail the composition because authority over A2.45 cannot be temporary while authority over the other four categories is durable.

Seventh, conflict structure must be architecturally inspectable as authoritative content. Inspection through vendor-specific tooling, system-internal-only APIs, or deployment-private interfaces fails the composition because authoritative content per A1.08 is inspectable on architectural terms, not on operator-specific terms.

Eighth, cell-mediated resolution per A2.14 must operate on authoritative conflict structure. Resolution that bypasses A2.45 — for example, by reading conflicts from a cache, an external service, or agent memory — fails the composition because the resolution architecture must operate over what the substrate authoritatively says is in conflict.

These eight forced decisions are jointly distinguishing. A deployment that satisfies A1.03 and A1.08 individually but fails any one of them fails the composition.

## 4. Anti-patterns specifically violating the composition

The composition is violated by a family of anti-patterns that share a structural shape: conflict authority migrates somewhere other than substrate authoritative content per A2.45. The migrations are distinct enough to merit separate names.

**Silent conflict resolution (A3.08)** is the canonical composition violation. Conflicts are resolved automatically without ever being preserved as authoritative substrate content; A2.13 preservation may be partially defeated and A2.45 authority is never established. The composition fails because conflicts never enter the source of truth.

**Contradiction collapse by automation (A3.10)** violates the composition through automated mechanisms — CRDT primitives, last-write-wins policies, ML-driven resolution — that resolve conflicts without authorization from rules per A2.46. Resolution occurs, so A1.03 may appear partially satisfied, but the resolution is not rule-mediated authoritative content; the composition fails because the resolution architecture bypasses substrate authority over A2.45 and A2.46 jointly.

**LLM-as-source-of-truth for conflict resolution (A3.13)** violates the composition specifically when an LLM exercises authority over what is in conflict and how it should be resolved. Authority for A2.45 migrates to the LLM. The composition fails because the source of truth's authority over conflict has moved into a non-substrate location.

**Agent memory as source of truth for conflict structure (A3.14)** violates the composition when contradictions detected by agents are held in agent memory rather than substrate. The deployment may have rich substrate content for the four non-conflict categories, but A2.45 fails because conflict authority lives in agent memory.

**External tool state authoritative for conflict (A3.17)** violates the composition when vendor conflict-resolution APIs, external mediation systems, third-party "consensus engines," or workflow-engine conflict primitives hold conflict state authoritatively. A2.45 fails because authority over "what is in conflict" lives in external tools.

**Caches authoritative for resolution (A3.18)** violates the composition when resolution caches serve resolved-state without consulting substrate-authoritative resolution. Cached answers function as the operative answer; A2.45 fails through cache-authoritative resolution.

**Adjacent component as substrate substitute for conflict structure (A3.23)** violates the composition when a vector database, knowledge graph, RAG corpus, or other adjacent component holds conflict structure architecturally as the primary location. A2.45 authority lives in the substitute rather than substrate.

**Conflict-as-metadata** violates the composition when contradictions are stored as warning flags, exception logs, anomaly markers, or debug artifacts about substrate state rather than as content of substrate state. The deployment may have rich metadata, but the metadata is not authoritative for A2.45; the composition fails because the metadata's status is "about substrate" rather than "of substrate."

**Conflict-resolution-as-implementation-detail** violates the composition when resolution rules live in implementation code, vendor configuration, or framework defaults rather than as substrate-resident authoritative content per A2.46. Rules exist, but they are not part of the source of truth; the composition fails because resolution does not operate under authoritative rules.

**Conflict-aging-without-authority** violates the composition when persistent conflicts are aged out by non-rule mechanisms — for example, "conflicts older than 30 days are auto-resolved" embedded in implementation logic. The aging operates outside authoritative rules per A2.46; the composition fails because conflict-handling-aging is not rule-mediated.

These anti-patterns can co-occur. A deployment may exhibit silent resolution (A3.08), automation collapse (A3.10), and conflict-as-metadata simultaneously, with each migration moving conflict authority to a different non-substrate location. They are jointly the failure space of the composition.

## 5. What the composition is NOT

Four adjacent patterns are commonly conflated with substrate-resident conflict structure and should be distinguished.

Not conflict-preservation-as-metadata. Architectures that preserve conflicts as metadata — warning flags, exception logs, anomaly markers — do not satisfy the composition. The composition forces conflicts to be authoritative substrate content, not annotations about substrate content.

Not substrate-authoritative-with-conflicts-as-exceptions. Architectures where substrate is authoritative for the four non-conflict categories while conflicts are handled as exceptions outside the source of truth do not satisfy the composition. The composition forces A2.45 to be operationalized as part of the same source of truth as the other four categories.

Not conflict-resolution-through-vendor-mechanisms. Vendor APIs, third-party "consensus engines," and external mediation systems may resolve conflicts but do not satisfy the composition if conflict structure lives in vendor systems. The composition forces conflict structure to be substrate-resident authoritative content regardless of what executes the resolution.

Not implicit conflict-resolution rules. Resolution logic embedded in implementation code, vendor configuration, or framework defaults does not satisfy the composition. The composition forces resolution rules to be authoritative content per A2.46.

## 6. Why the composition is load-bearing

The composition is the architectural answer to "where do conflicts live?" in CKS — in substrate, authoritatively, per A2.45. It is referenced explicitly in §11.3 of the source paper, where Category 3 of the source-of-truth commitment names "what contradictions are unresolved" as a category for which the substrate is authoritative; A4.08 operationalizes that category through A2.17. It distinguishes CKS from conflict-as-exception architectures dominant in 2024–2026 distributed AI systems. It is the supporting commitment for A4.07 (conflict-provenance: provenance applies to conflicts because conflicts are authoritative content), for A4.05 (AI-mediated authority preservation: AI cells operate on authoritative conflict structure rather than exercising authority over it), and for A4.01 (governance-against-authority: humans govern conflicts because A1.08's authority reaches A2.45). It produces operationally distinct anti-pattern instantiations: the family of A3 anti-patterns named in §4 each violate the composition through a different conflict-authority migration mechanism, and a single individual-commitment frame does not capture the family.

The composition extends across all conflict-related substrate operations. When conflicting writes per A2.13 produce contradictions, the contradictions *are* authoritative content per A2.45 from the moment of creation; contradiction edges per A2.17 persist as authoritative artifacts across the deployment lifecycle; cell-mediated resolution per A2.14 operates on authoritative conflict structure under rules per A2.46 that are themselves authoritative; humans per A2.15 inspect authoritative conflict structure through governance rights. At each stage the composition holds, or the architecture is no longer doing what CKS commits to do.

## 7. Operational test

A deployment satisfies the A1.03 × A1.08 composition if all of the following are true at all times during the deployment's existence.

1. Contradictions per A2.17 are authoritative substrate content addressing A2.45 — they are part of the source of truth, not metadata about it.
2. "What is in conflict" per A2.45 has architectural specification through contradiction edges, with stable addresses per A2.59.
3. Conflict-resolution rules per A2.46 are authoritative substrate content governing conflict-handling per A2.14.
4. Humans can inspect, modify, override, and rule-author conflict structure through the governance rights per A2.01–A2.04 applied to A2.45.

Three sharpening properties operationalize the test for deployment review.

*Substrate-resident-contradiction test.* Examine where conflict structure lives. Conflicts in metadata, external tools, agent memory, caches, or adjacent components indicate composition failure even when conflicts are nominally preserved.

*A2.45-authoritative-specification test.* Examine the deployment's conflict architecture. Absence of an architectural mechanism for representing authoritative conflict structure indicates composition failure even when preservation per A2.13 is technically met.

*Conflict-governance-affordance test.* Attempt the four governance operations on conflict structure. Inability to inspect, modify, override, or rule-author conflicts indicates composition failure even when conflicts are nominally authoritative.

A deployment that satisfies (1)–(4) and the three sharpening tests satisfies the composition.

The one-sentence test. If a deployment's contradictions per A2.17 are authoritative substrate content addressing A2.45, with "what is in conflict" architecturally specified through contradiction edges, conflict-resolution rules per A2.46 authoritative content governing conflict-handling per A2.14, and humans able to govern conflict structure through inspect, modify, override, and rule-author rights per A2.01–A2.04 applied to A2.45 — the deployment satisfies the A1.03 × A1.08 composition. The emergent architectural property is substrate-resident conflict structure, with conflicts as first-class authoritative state distinguishing CKS from conflict-as-exception architectures and supporting A4.07 conflict-provenance, A4.05 AI-mediated authority preservation for conflict-handling, and A4.01 governance-against-authority for conflict structure.

## 8. Conclusion

The composition of A1.03 and A1.08 produces an architectural property that neither commitment yields alone: substrate-resident conflict structure. Contradictions become first-class content of the source of truth, not metadata about it; "what is in conflict" gains architectural specification; conflict-resolution rules join the authoritative content the deployment operates under; conflict structure becomes governable through the standard governance rights. The composition is what makes conflict-handling architecturally first-class in CKS rather than implicit in the foundational commitments.

Implementations that satisfy A1.03 individually (preservation with cell-mediated resolution) or A1.08 individually (substrate authoritative for non-conflict state) but fail the composition produce systems where conflict-handling is not architecturally first-class — conflicts as metadata, conflicts in agent memory, conflicts in external tools, conflicts collapsed by automation, conflicts in adjacent component substitutes. A4.08 names the composition as standalone so that downstream readers have a precise specification of CKS's substrate-resident conflict structure and can identify deployments that satisfy or fail it.

A4.08 follows A4.07 in completing the conflict-handling composition coverage in Phase A4. Together A4.07 (conflict + retraceability, producing conflict-provenance) and A4.08 (conflict + source-of-truth, producing substrate-resident conflict structure) cover how A1.03 composes with the two foundational commitments most directly relevant to its operation. Subsequent Phase A4 notes will formalize approximately twenty-two additional architecturally significant composition pairs from the C(16,2) = 120 possible pairs of the sixteen foundational A1 commitments — including A1.05 × A1.06 (tool-agnosticism × linear-cost), A1.05 × A1.08 (tool-agnosticism × source-of-truth), and A1.04 × A1.10 (mediator × determinism). The substrate-resident conflict structure formalized here is one architectural property among many that the composition pairs name.

---

## Source paper

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Substrate-Resident Conflict Structure: The Composition of Conflict-as-First-Class and Substrate-as-Source-of-Truth in the Coordination Knowledge Substrate Pattern.* May 6, 2026. ORCID: 0009-0004-8065-3235.
