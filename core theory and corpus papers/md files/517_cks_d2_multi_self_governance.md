# Multi-Self FAI Event Governance

**Derivation Note D2.22 — Series D, Phase D2, Note #517**
CKS Theory Derivation Notes

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** CC BY 4.0

---

**Attribution:** This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## 1. Position in the Derivation Series

D2.22 is an operational decomposition of D1.07, the foundational sub-commitment establishing that n-ary cardinality is an architectural property of the shared substrate and the Full Aspect Integration (FAI) operation. D1.07 commits that any number of Selves can participate in a single FAI event, with two-Self FAI as the simplest instance. D2.22 develops the governance dimension of that architectural fact: specifically, which governance obligations scale as N grows and which remain constant regardless of N.

This distinction matters for prior-art purposes. The constant-architecture result closes adversarial claims that coordinating three or more AI-governed Selves requires novel architectural commitments beyond what two-Self FAI already establishes. The linear-scaling result establishes that governance overhead increases proportionally with N rather than compounding exponentially — a result consistent with Paper 1's linear-cost commitment extended to the inter-Self scope.

---

## 2. What Scales With N: Five Governance Dimensions

When a FAI event involves N participating Selves, five governance dimensions scale with N. Each is described below with the scaling character — linear in all five cases.

### 2.1 Joint Authorization Complexity

Every FAI event requires authorization from the governance structures of all participating Selves before the shared substrate is constructed. At N=2, joint authorization involves two governance structures reaching agreement on the configuration. At N=3, three governance structures must authorize. At N=k, k governance structures must authorize.

The authorization mechanics are themselves configurable as substrate content under joint authority (Claim 5 of Paper 3). Governance can implement N-party authorization through consensus, through majority threshold, through delegated authority per D2.12, or through any other mechanics the participating Selves' governance jointly adopts. The standing configuration established in D2.21 provides a particularly effective mechanism for recurring N>2 events: rather than negotiating N-party authorization fresh for each event, the standing configuration pre-establishes the authorization mechanics, reducing per-event coordination overhead. Without a standing configuration, each N>2 event requires its authorization procedure to be negotiated among N governance structures, which is the principal source of N-sensitive governance overhead.

The scaling character here is linear: each additional participating Self adds one governance structure to the authorization scope. Authorization complexity does not compound multiplicatively as N grows, because the authorization is over the configuration substrate, not over all pairwise combinations of participant capabilities.

### 2.2 Contribution Complexity

Each of the N participating Selves contributes governance-selected aspects to the shared substrate. The shared substrate during the event contains N sets of contributed aspects. Merge operations combine N contributions rather than two. Conflict detection during merge must compare across all N contributions — not just the pairwise comparison sufficient at N=2.

The governance obligation this creates is that the configuration must specify, for each of the N participating Selves, which aspects that Self contributes. A configuration that specifies contributions for only N-1 Selves is incomplete. The contribution scope must explicitly enumerate all N participants.

Conflict density — the number of conflicts the conflict-handling mechanism must process — typically increases with N as more governance approaches and more accumulated experience are combined in the shared substrate simultaneously. At N=2, conflicts arise at the boundary of two contribution sets. At N=3, conflicts can arise between any pairing across the three contribution sets, as well as at three-way junctions where all three contributions bear on the same coordination structure. The three-tier conflict-handling mechanism (D0.03) handles all surfaced conflicts regardless of density and regardless of N; the governance implication is that the configuration should anticipate elevated conflict density at higher N and ensure the conflict handling capacity is adequate.

### 2.3 Conflict Registry Complexity

The conflict registry (D2.13) records all conflicts surfaced during the FAI event, with attribution identifying which participating Self's contribution generated each side of each conflict. At N=2, attribution is binary: each conflict side traces to Self A's contribution or Self B's contribution. At N=3, attribution must correctly identify among three contributing Selves. At N=k, attribution must correctly identify among k contributing Selves.

Attribution complexity increases linearly with N because the number of potential attribution targets grows by one for each additional participating Self. The three-tier handling logic — preserve as substrate-level state by default; resolve via configured orchestration substrate; escalate to humans across joint authority of all participating Selves' governance — applies at every tier to every conflict regardless of N. What scales is not the handling mechanism but the richness of attribution the registry must maintain.

For governance verification purposes: an observer auditing an N=3 FAI event's conflict registry should be able to determine, for every conflict record, which of the three contributing Selves produced each conflict side. A conflict record that does not specify attribution correctly across all three Selves is a registry integrity failure, not merely an attribution gap.

### 2.4 Home Perimeter Integrity Verification

Before the shared substrate is constructed for a FAI event, the home perimeter of each participating Self must be verified as intact (D2.17). The verification establishes that each participating Self's governance structure is functioning and that the configuration the participating Self has authorized reflects that Self's actual home governance authority.

At N=2, two home perimeters must be verified. At N=3, three. The verification scope scales linearly: each additional participating Self adds one home perimeter to the pre-event verification process. There is no shortcut by which verifying N-1 perimeters establishes anything about the Nth. Each perimeter is sovereign and must be verified independently under its own governance structure.

The governance risk of incomplete perimeter verification is asymmetric: proceeding with an unverified home perimeter means the FAI event's configuration may rest on governance authorization that has not been confirmed to reflect that Self's actual authority. The evolution feed outputs that the unverified Self subsequently ingests into its home substrate would then propagate content through an unconfirmed governance pathway. Home perimeter integrity verification is therefore a non-negotiable pre-event obligation that scales with N but cannot be amortized or skipped.

### 2.5 Evolution Feed Recipients

When the shared substrate dissolves at the close of a FAI event, content propagates to each participating Self's home substrate per Claim 4's four-locus evolution-feed mechanism. At N Selves, there are N distinct evolution feed recipients. Governance must track N home ingestion events and N sets of home governance authorization for absorption of the FAI-derived content.

Each participating Self's home governance independently authorizes what that Self absorbs from the FAI dissolution feed. Asymmetric ingestion holds: Selves A, B, and C participating in the same N=3 event may take different content from the dissolution, under the direction of their respective home governance authorities. The governance record must reflect all N absorption events with their respective governance authorizations, not merely a single consolidated record.

The layer-routing rule applies identically at every participating Self's home perimeter regardless of N: DNA-layer content feeds DNA evolution at home; action-layer content feeds action-feedback evolution at home; instinct evolution takes no FAI input by architectural commitment. The rule does not vary with N.

---

## 3. What Does Not Scale: Architectural Commitments Constant Across All N

The following architectural elements are invariant with respect to N. Adding participating Selves does not alter, extend, or replace any of these commitments.

**The shared-substrate architecture and its six Paper 1 commitments** hold within scope for any N. The substrate is the medium of coordination; governance is not embedded in the LLM; conflicts are first-class addressable state; humans hold authority; labor-authority distinction applies; path retraceability is maintained. None of these vary with N.

**The three-tier conflict-handling mechanism** (D0.03) applies to all conflicts surfaced during the FAI event regardless of how many Selves contributed content and regardless of conflict density. The three tiers — preserve as substrate-level state by default; resolve via configured orchestration substrate; escalate to humans across joint authority of all participating Selves' governance — are the complete mechanism at any N.

**The exchange-bounding commitment** (D1.10) holds at any N: DNA-layer content and action-layer content exchange through the shared substrate; LLM weights and instinct-layer content do not. The boundary does not move as more Selves participate.

**The three FAI pattern variants** (D1.09) — union, selective merge, lineage-preserved union — are available at any N. Cardinality does not introduce additional pattern variants or remove existing ones.

**The dissolution and persistence governance** (D1.01 and D1.04) apply at any N. The shared substrate dissolves at event close; the persistence policy is substrate content configurable per event; what persists where is determined by the participating Selves' joint governance.

**Each Self's home perimeter sovereignty** (D1.03) is unaffected by how many other Selves participate in a given FAI event. Self C's home governance authority over Self C's home substrate is not diminished or restructured by the fact that Selves A, B, D, and E are also participating. Home perimeter sovereignty is an invariant of the architecture, not a function of N.

The invariance result is the core prior-art claim this note secures. A system that coordinates N AI-governed Selves using the shared-substrate and FAI architecture inherits all of the architectural commitments from the two-Self case without modification. No additional architectural primitive is required at N=3, N=5, or any N>2. Claims 1 through 5 of Paper 3 hold at any N.

---

## 4. Practical N Threshold

The architecture specifies no maximum N. The practical upper bound on N for any given FAI event is determined by the governance capacity of the participating Selves' organizations — specifically, by the human and organizational bandwidth available to execute N-party authorization, N-contribution configuration, N-way home perimeter verification, and N-recipient evolution feed tracking in a coherent and timely manner.

As N grows, the governance coordination overhead grows linearly across all five dimensions in §2. For large N, this overhead can become the binding constraint on whether a FAI event can be conducted at adequate governance quality. The architectural answer to large-N governance overhead is the standing configuration (D2.21): a pre-established, reusable configuration that covers the authorization mechanics, contribution scope, conflict handling routing, and evolution feed structure for a defined set of participating Selves. Under a standing configuration, each individual FAI event does not require N-party authorization to be negotiated from scratch; the governance investment is made once in authoring and adopting the standing configuration, and individual events execute under it.

The standing configuration is particularly valuable for recurring N>2 events: consortia of organizations whose Selves participate in periodic joint FAI events, or multi-party coordination patterns where the same N Selves interact regularly. The standing configuration does not reduce the N-linearly-scaling governance verification obligations — home perimeter verification, evolution feed tracking — but it substantially reduces the N-sensitive authorization overhead.

The practical N threshold is therefore not fixed architecturally. It is governance-determined per deployment context, and it is raisable through governance investment in standing configurations and in the human and organizational infrastructure to support multi-party coordination at the desired N.

---

## 5. Two-Self as Minimum Viable Unit

N=2 is the minimum configuration that instantiates all of Paper 3's Claims 1 through 5. Two-Self FAI is not a simplified or partial case: it is the complete architecture. Every governance consideration described in §2 exists at N=2 as its simplest form — two-party joint authorization, two contribution sets in the shared substrate, conflict attribution between two Selves, two home perimeters to verify, two evolution feed recipients. N>2 adds governance complexity in the five dimensions above but does not add architectural commitment.

This framing matters for how N>2 FAI events are positioned relative to the prior art the two-Self case establishes. A N=3 event is not architecturally distinct from a N=2 event — it is the same architecture operating over three participating Selves rather than two. The governance configuration is larger; the architecture is identical.

---

## 6. Anti-Pattern: N-Blind Configuration

**Name:** N-Blind Configuration

**Definition:** Conducting a N>2 FAI event using a configuration designed and validated for N=2 without updating the joint authorization mechanics, contribution scope, conflict handling routing, and evolution feed structure for all N participating Selves.

**Specific form — N=2 configuration applied to N=3:** The most dangerous instance is a N=2 configuration applied to a N=3 event. In this case: the joint authorization mechanics may specify only two-party authorization, leaving the third Self's governance participation either unauthorized or tacitly assumed. The contribution scope may enumerate only two contributing Selves' aspects, leaving the third Self's contributions either absent or unattributed. The conflict registry attribution may be structured for binary attribution, making correct attribution of conflicts involving three contributing Selves structurally impossible. One home perimeter may be unverified. The evolution feed tracking may record only two ingestion events.

The N-blind failure is not merely a documentation gap. An unauthorized governance participation means the FAI event proceeds without confirmation that the third Self's governance structure has authorized the configuration — a governance integrity failure, not an administrative omission. An unverified home perimeter means evolution feed content propagates into that Self's home substrate through an unconfirmed governance pathway. A binary-attribution conflict registry means the conflict record for the N=3 event is irrecoverably incomplete.

**How to avoid:** The configuration must be authored for the specific N of the intended event. If a N=2 standing configuration exists and a third Self is to be added to a recurring event pattern, the standing configuration must be explicitly revised to enumerate the third Self across all five governance dimensions: authorization mechanics, contribution scope, conflict registry attribution, home perimeter verification scope, and evolution feed recipient tracking. The revision is itself substrate content under joint authority per Claim 5, authored by the participating Selves' governance jointly.

---

## 7. Operational Test

**Test for a N=3 FAI event:** An observer with access to the FAI event's configuration substrate and post-event records should be able to verify all of the following.

*Authorization:* Three distinct governance structures are identified in the configuration as authorization parties. The configuration records authorization from all three before the shared substrate was constructed.

*Contribution tracking:* Three contributing Selves' aspect sets are enumerated in the configuration, with each Self's governance-selected contributions listed. The shared substrate record reflects three contribution sets.

*Conflict registry attribution:* The conflict registry for the event attributes each conflict side to one of the three contributing Selves. No conflict record contains unattributed sides.

*Home perimeter verification:* Three home perimeter verification records exist, one per participating Self, completed prior to shared substrate construction.

*Evolution feed records:* Three evolution feed ingestion records exist at event dissolution, one per participating Self, each reflecting that Self's home governance authorization for absorption.

A N=3 FAI event that passes all five checks is correctly configured as a three-party event. A N=3 FAI event that fails any check exhibits N-blind configuration at the dimension of the failed check.

---

## 8. Inheritance Accounting

D2.22 inherits from:

- **D1.07** (n-ary cardinality as architectural property) — the parent sub-commitment this note operationally decomposes.
- **D1.02** (six Paper 1 commitments holding within shared substrate scope) — the source of the invariance claim in §3.
- **D0.03** (three-tier conflict-handling mechanism) — the source of the constant conflict-handling claim in §3.
- **D1.10** (exchange-bounding commitment) — the source of the constant exchange-boundary claim in §3.
- **D1.09** (three FAI pattern variants) — source of the pattern-variant invariance claim in §3.
- **D2.12** (delegated authority mechanics) — referenced in §2.1 as an authorization-mechanics option.
- **D2.13** (conflict registry) — the conflict attribution record described in §2.3.
- **D2.17** (home perimeter integrity verification) — the verification obligation described in §2.4.
- **D2.21** (standing configuration) — the mechanism cited in §2.1 and §4 as the governance tool for managing N>2 recurring events.
- **Paper 1 linear-cost commitment** (D1.28 Rung 5) — the linearity of governance scaling described in §2 is consistent with Paper 1's linear-cost commitment extended at the inter-Self scope.

The fresh content in D2.22 is the explicit partitioning of governance obligations into the five N-scaling dimensions (§2) versus the invariant architectural commitments (§3), together with the N-blind configuration anti-pattern (§6) and the N=3 operational test (§7). This partitioning is a D2-level operational decomposition of the cardinality property D1.07 establishes; it is not present at the sub-commitment level.

---

*End of D2.22.*
