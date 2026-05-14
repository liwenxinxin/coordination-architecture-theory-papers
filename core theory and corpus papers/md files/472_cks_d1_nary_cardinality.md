# N-Ary Cardinality as an FAI Architectural Property

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI) is an n-ary operation: any number N of CKS-governed Selves can participate in one FAI event. The architecture does not cap cardinality at two. Two-Self FAI (N=2) is the simplest independently claimable instance — it satisfies the minimum governance infrastructure required to instantiate all of Paper 3's Claims 1–5 — but the same architectural commitments hold at any N. This note formalizes n-ary cardinality as an architectural property of FAI rather than an implementation detail or deployment option. It develops four governance dimensions that scale with N — joint authority, contributing aspects, home perimeters, and evolution feed outputs — and shows that each scales under the same commitments rather than requiring new ones. It demonstrates that two-Self FAI is architecturally complete and independently claimable as prior art. It states that the cardinality of any specific FAI event is governance-configured per event, not hardwired as system configuration. It identifies four failure modes this sub-commitment defends against, and provides an operational test applicable at N=3.

---

## 1. The sub-commitment stated

Paper 3 Claim 2 establishes Full Aspect Integration as the canonical operation over the shared substrate. Within that claim, one architectural property warrants separate formalization: cardinality is n-ary.

The n-ary cardinality commitment states: any number N of CKS-governed Selves can participate in a single FAI event. The architecture does not specify a maximum. The architecture does specify a minimum — N=1 is not an FAI event, because FAI is inter-Self coordination; one-Self combination remains intra-Self territory governed by Paper 2 — but above that floor, cardinality is architecturally unbounded and governance-determined per event.

This is an architectural commitment, not an implementation aspiration. An architecture that permits only two-party FAI leaves multi-party inter-Self coordination as unoccupied territory. An architecture that makes multi-party FAI available as an implementation variant treats cardinality as a product feature rather than an architectural property. Paper 3 commits to n-ary cardinality as architecture: the commitments established for N=2 hold at every N above 2, and no fresh commitments are required as N increases.

The prior-art value of the commitment is dual. First, it places two-party inter-Self coordination — the N=2 case — as a named, complete, independently claimable instance. Second, it places multi-party inter-Self coordination — every N>2 case — under the same architecture without requiring any party to introduce additional commitments to claim novelty at higher cardinality.

---

## 2. Four governance dimensions at N-ary scope

As N increases, four governance dimensions scale. Each scales under the existing architectural commitments rather than requiring new ones. The four dimensions correspond to the four structural properties Paper 3 establishes at the two-Self scope and generalizes to any N.

### 2.1 Joint authority at N-party scope

In two-Self FAI, the shared substrate is jointly governed by two governance structures — the governance authorities of the two participating Selves. Joint authority means that the configuration of the shared substrate, including what each Self contributes, how the merge proceeds, and what happens to conflicts, is substrate content authored under the authority of both governance structures.

At N-party scope, the same principle extends: the shared substrate is jointly governed by N governance structures. The configuration substrate specifies how N-party joint authority is exercised. Which of the N governance structures must authorize the configuration before construction begins — the approval mechanics — is itself governance-configurable per event. N-party joint authority is not a fresh architectural commitment; it is the two-party joint authority commitment applied at N-party scope under the same principle: all participating Selves' governance authorities hold rights over the shared substrate.

The scalability of this principle is what makes n-ary cardinality architecturally tractable rather than governance-intractable. A system that hardwired two-party joint authority as a special mechanism — rather than expressing it as an instance of the general N-party commitment — would require architectural extension at every new cardinality. The n-ary commitment avoids that by making the two-party case an instance rather than a baseline.

### 2.2 N contributing aspects

In two-Self FAI, each of the two participating Selves contributes its governance-selected aspects to the shared substrate. The shared substrate's content during the event is the governed combination of both Selves' contributed aspects. Conflicts surfaced during merge are handled under the three-tier mechanism established by Paper 3 Claim 3.

At N-party scope, each of the N Selves contributes its governance-selected aspects. The shared substrate's content at any point during the event is the governed combination of all N Selves' contributed aspects. Conflict handling continues to operate under the three-tier mechanism — the same three tiers apply regardless of how many Selves' contributions are in scope. The mechanism's preserve tier operates over contributions from N sources; its resolve tier applies orchestration rules authored under joint authority across N governance structures; its escalate tier surfaces conflicts to the joint authority of all N participating governance structures.

Nothing about the three-tier mechanism requires knowing N in advance. It is an N-agnostic conflict-handling architecture at the Claim 3 level; the n-ary cardinality commitment at the Claim 2 level is consistent with and relies on that N-agnosticism.

### 2.3 N home perimeters

In two-Self FAI, each participating Self maintains its home perimeter throughout the event. The shared substrate exists across the inter-Self perimeter, which spans both home perimeters simultaneously. At dissolution, both home perimeters continue operating independently; the dissolution does not collapse one into the other.

At N-party scope, each of the N participating Selves maintains its home perimeter throughout the event. The inter-Self perimeter spans all N home perimeters simultaneously. At dissolution, all N home perimeters continue operating independently. The perimeter-spanning property established by Paper 3 Claim 1 does not require a two-perimeter topology; it is a general property of the shared substrate that holds at any N. The shared substrate spans however many home perimeters the event's participating Selves bring; its dissolution leaves each intact.

The independence of home perimeters at dissolution is particularly important at higher N because it forecloses the misreading that multi-party FAI functions as a merger or absorption operation. N participating Selves at dissolution remain N distinct Selves with N intact governance structures, each receiving its own evolution feed outputs from the shared substrate per Claim 4.

### 2.4 N evolution feed outputs

In two-Self FAI, the hand-off at the FAI dissolution boundary delivers evolution feed outputs to each of the two participating Selves independently. Each Self's home governance determines what it ingests. The four-locus evolution feed structure — established by Paper 3 Claim 4 — applies to each Self independently at its own home perimeter.

At N-party scope, each of the N Selves receives evolution feed outputs from the shared substrate at dissolution. The four-locus structure applies independently to each of the N Selves; each Self's home governance determines what that Self ingests. Asymmetric ingestion — the property that different Selves may take different things from the same FAI event, because each Self's governance applies independently to the outputs available to it — holds at any N. The asymmetry is not a two-party property; it is a general consequence of per-perimeter governance applied to the dissolution hand-off.

---

## 3. Two-Self FAI as the simplest independently claimable instance

The two-Self case is architecturally significant beyond being the lowest-cardinality instance. N=2 is the minimum configuration that instantiates all of Paper 3's Claims 1–5 simultaneously:

- **Claim 1 (shared substrate):** a shared substrate spanning two home perimeters instantiates the perimeter-spanning property, the construction-as-temporary commitment, and the dissolution commitment.
- **Claim 2 (FAI):** two Selves contributing aspects, with full-merge default and governance-configurable pattern variants, instantiates the FAI mechanism.
- **Claim 3 (three-tier conflict handling):** conflicts surfaced during merge from two contributing Selves instantiate the three-tier mechanism, including escalation across joint authority.
- **Claim 4 (four-locus evolution feed):** dissolution delivering outputs to two Selves, each with independent home governance, instantiates the asymmetric four-locus feed.
- **Claim 5 (configuration as substrate content):** the configuration of the N=2 event is substrate content under joint authority of two governance structures, with recursive applicability.

N=2 is not an incomplete instance waiting to be generalized. It is a complete instance of the full Paper 3 architecture. The n-ary commitment does not improve the two-Self case; it extends the architectural commitments to higher cardinalities without adding to them. This is what makes two-Self FAI independently claimable as prior art: the N=2 case establishes all of the architectural commitments in full; every higher-N case is those same commitments at greater participation count.

The practical importance of this framing is defensive. A party that observes only N=2 deployments and then develops N=3 coordination should not be able to claim that N=3 inter-Self coordination requires architecture beyond what N=2 establishes. The n-ary cardinality commitment anticipates and forecloses that claim: Paper 3 commits to all N above 1, with N=2 as the simplest instance, and the same commitments hold throughout.

---

## 4. Cardinality as governance configuration per event

The n-ary architectural commitment does not mean all FAI events have the same cardinality. Different FAI events may have different N; the architecture supports any N while governance determines which N is appropriate for each specific coordination task.

Cardinality for a specific FAI event is governance-configured per event. The configuration substrate specifies which Selves participate, establishes the joint authority approval mechanics for those Selves' governance structures, and determines what each contributing Self's aspects and merge behavior will be. This configuration is substrate content under joint authority per Paper 3 Claim 5's recursive applicability. It is not a system-level parameter set at deployment time; it is event-level substrate content authored and governed per event.

This has a precise implication: a system that hardwires cardinality — either by constraining all FAI events to N=2 or by fixing N at any other value across events — does not instantiate the n-ary cardinality commitment as an architectural property. A system that permits cardinality to vary across events under governance does. The architectural commitment is the availability of governance-configurable N per event, not any specific N.

The governance-configurability of cardinality also means the architecture does not require advance planning for a specific maximum N. Because cardinality is per-event substrate content, governance can configure a new N for a new coordination task using the same configuration mechanism that governs every other dimension of the FAI event. Scalability in cardinality is substrate-content configurability, not system-level extensibility.

---

## 5. Four failure modes this sub-commitment defends against

The n-ary cardinality commitment is formalized against four specific failure modes.

**Failure mode 1 — Binary-only inter-Self coordination.** An architecture that commits only to two-party coordination leaves multi-party inter-Self coordination as unoccupied territory available for novel claims. The n-ary commitment forecloses this by establishing multi-party FAI under the same commitments as two-party FAI. A party developing N=3 or higher inter-Self coordination cannot claim that the architecture is novel relative to what Paper 3 establishes.

**Failure mode 2 — Multi-party FAI as architecturally novel relative to two-party FAI.** Even if a party accepts that two-party inter-Self coordination is established, it might claim that multi-party coordination requires additional architectural commitments — a richer conflict-handling mechanism, a new joint-authority structure, a different evolution feed model — and that those additions constitute novel invention. The n-ary commitment defends against this by showing that the same four governance dimensions scale from N=2 to any N under the same commitments. No fresh commitments are required.

**Failure mode 3 — Cardinality as hardwired system configuration.** An architecture that fixes cardinality at the system level — determining N at deployment rather than per event — treats cardinality as an implementation parameter rather than a governance-configurable property. Such an architecture is a restricted instance of the n-ary commitment, not a novel alternative to it. The per-event governance-configuration of cardinality is the architectural commitment; hardwired cardinality is a special case that Paper 3's architecture subsumes.

**Failure mode 4 — Multi-party joint authority as requiring novel governance mechanisms.** A party might claim that joint authority at N>2 requires governance structures not present in the two-party case — majority-vote mechanisms, quorum requirements, dedicated multi-party arbitration layers. The n-ary joint authority commitment forecloses this by establishing N-party joint authority as the same principle as two-party joint authority, with approval mechanics (including whatever voting or quorum structure governance configures) as governance-configurable substrate content rather than architectural-layer additions.

---

## 6. Operational test

For an FAI event with N=3 participating Selves — call them Self A, Self B, and Self C — an observer can verify that the n-ary cardinality commitment is instantiated by examining three observable properties:

**Home perimeter integrity.** At any point during the event and at dissolution, each of the three Selves' home perimeters remains intact and independently operational. No content from the shared substrate has been absorbed into any Self's home perimeter without passing through that Self's governance-determined ingestion. No Self's home perimeter has been collapsed into another's. Dissolution leaves three intact, independent governance structures operating at their home perimeters.

**Shared substrate composition.** The shared substrate contains contributions from all three Selves. Each contribution is traceable to the Self whose governance selected the aspects contributed. Conflicts surfaced during merge from any combination of the three Selves' contributions are represented as first-class addressable substrate state. The shared substrate does not contain content attributable only to two of the three Selves, unless the third Self's governance specifically contributed nothing — in which case that governance decision is itself substrate content.

**Joint authority configuration.** The configuration substrate specifies how all three Selves' governance authorities participate in the joint authority over the shared substrate. The approval mechanics — which of the three governance structures must authorize the configuration before construction begins — are present as substrate content. An observer can read the configuration and determine what authorization from each of the three governance structures was required and obtained. No configuration decisions about the shared substrate were made outside the joint authority of the three participating governance structures.

A system in which any of these three properties fails for a three-party event does not instantiate the n-ary cardinality commitment, regardless of whether it is labeled as multi-party coordination.

---

## 7. Conclusion

N-ary cardinality is an architectural property of Full Aspect Integration, not an implementation capability or a deployment option. The commitment has three components: any N above 1 is supported; the same four governance dimensions — joint authority, contributing aspects, home perimeters, evolution feed outputs — scale to any N under the same commitments established at N=2; and the cardinality of any specific FAI event is governance-configured per event as substrate content under joint authority. Two-Self FAI is the simplest independently claimable instance: N=2 instantiates all of Paper 3's Claims 1–5 in full. Multi-party FAI is not architecturally novel relative to two-party FAI; it is the same architecture at higher participation count. Cardinality as hardwired system configuration is a restricted instance of this commitment; per-event governance-configured cardinality is the architectural commitment.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *N-Ary Cardinality as an FAI Architectural Property.* May 14, 2026. ORCID: 0009-0004-8065-3235.
