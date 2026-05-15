# Composition Pair 2: Standing Configurations and Multi-Self Events

**Derivation Note D4.03 — Series D, Phase D4 (Composition Pairs)**
**Note #608 in the CKS Defensive-Publication Series**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

This note formalizes the composition of two Paper 3 commitments: Standing Configurations (D2.21), which define reusable jointly-authorized governance templates for recurring Full Aspect Integration (FAI) relationships, and Multi-Self FAI Governance (D2.22), which specifies the governance requirements for FAI events involving more than two participating Selves (N > 2). The non-obvious result of placing these two commitments in the same governance scenario is that bilateral standing configurations — configurations authorized for N = 2 relationships — do not automatically compose into a valid governance framework for an N = 3 event. Three bilateral configs covering each pair (A–B, A–C, B–C) leave a structural governance gap: three-way conflicts and three-way joint authorization are not specified by any bilateral config. Two valid approaches close the gap: authoring a single multilateral standing configuration that governs N = 3 events explicitly, or supplementing the existing bilateral configs with a lightweight N-specific supplement jointly authorized by all three Selves. The dynamic dimension of the pair — N-change governance — differs materially between the two approaches. Both approaches are established as prior art by this note.

---

## 1. Pair Identification

**Commitment A — Standing Configurations (D2.21):** A standing configuration is a reusable, jointly-authorized governance template that governs a recurring FAI relationship between a fixed set of participating Selves. The template specifies sharing scope, joint authorization rules, conflict-routing logic, and escalation paths for the relationship it covers, and it is authored once and applied to each instance of that FAI relationship without re-negotiation per event. Standing configurations exist at Claim 5 scope (configuration as substrate content) and are themselves substrate content under joint authority.

**Commitment B — Multi-Self FAI Governance (D2.22):** When an FAI event involves N > 2 participating Selves, governance requirements scale in a specific way: joint authorization must be N-party (not bilateral), sharing scope must cover all N Selves' contributions, and conflict-routing must address conflicts where all N Selves' content diverges simultaneously — conflicts that have no bilateral analog. The N-ary structure of Claim 2's cardinality commitment (FAI is defined for N ≥ 2) means multi-Self governance is not an edge case but an architectural commitment in the pattern.

These two commitments compose whenever an organization maintaining standing configurations for bilateral FAI relationships needs to conduct an FAI event with N > 2 participants drawn from that standing-configuration pool.

---

## 2. Governance Scenario Requiring Both Simultaneously

An organization maintains standing configurations for FAI relationships with multiple partners. It has three bilateral standing configurations in place: one governing the A–B relationship, one governing A–C, and one governing B–C. Each was authored as a bilateral instrument: N = 2 joint authorization, N = 2 sharing scope, bilateral conflict routing. Each is valid and operative for its respective bilateral FAI instances.

The organization now needs to conduct an FAI event involving Selves A, B, and C simultaneously, using the same shared substrate. The event is N = 3. Both commitments apply: the organization has standing configurations that should govern the event (D2.21 applies), and the event has N = 3 participants (D2.22 applies). The question is whether the three bilateral standing configurations, taken together, constitute valid N = 3 governance.

They do not — and the gap is structural.

---

## 3. Non-Obvious Governance Requirements from the Combination

### 3.1 Why Bilateral Configs Do Not Compose Automatically

A practitioner familiar with bilateral standing configurations might reason as follows: the A–B config covers A and B; the A–C config covers A and C; the B–C config covers B and C; together, every pair is covered. If every pair is covered, the event is governed. This reasoning is incorrect, and identifying why is the core contribution of this note.

Bilateral governance covers bilateral conflicts — conflicts where A's and B's contributions diverge (A–B), where A's and C's diverge (A–C), and where B's and C's diverge (B–C). An N = 3 FAI event also produces three-way conflicts: content where A, B, and C all contribute distinct values to the same aspect. No bilateral config specifies how three-way conflicts are routed, because the conflict type does not exist at N = 2 scope. Three bilateral configs, each complete at bilateral scope, leave the three-way conflict class ungoverned.

Similarly, bilateral governance covers bilateral joint authorization: A and B together authorize the A–B config; A and C authorize the A–C config; B and C authorize the B–C config. An N = 3 FAI event requires that all three Selves jointly authorize the governance framework for the event. Three bilateral authorizations are not a three-party authorization. A governance framework that requires A and B to authorize one instrument, A and C to authorize a second, and B and C to authorize a third has not established a single instrument that A, B, and C have all authorized together. The joint-authority requirement for N = 3 is not satisfied by the union of three bilateral authorizations.

The gap is therefore twofold: three-way conflict routing is absent, and three-way joint authorization is absent. Both absences are structural — not a matter of bilateral configs being incomplete in some respect that a careful reading could fill in, but a matter of N = 3 governance requirements being categorically different from N = 2 governance requirements.

### 3.2 Two Valid Approaches

**Approach A — Multilateral Standing Configuration:** The three Selves jointly author a single standing configuration that governs N = 3 FAI events explicitly. The multilateral config specifies: three-party joint authorization as the governance baseline, sharing scope covering all three Selves' contributions, conflict-routing logic for bilateral conflicts (A–B, A–C, B–C) and for three-way conflicts (A–B–C simultaneously), and escalation paths appropriate to three-party governance. The bilateral standing configs remain valid for bilateral FAI events involving any two of the three Selves; the multilateral config governs events where all three participate. This approach is structurally clean: a single governance instrument covers the N = 3 case completely. The cost is governance work upfront — the three Selves must jointly author, negotiate, and authorize the multilateral config before the first N = 3 event.

**Approach B — Bilateral Configs Plus N-Specific Supplement:** The existing bilateral standing configurations remain in place and continue to govern bilateral governance dimensions within the N = 3 event. A lightweight N-specific supplement is added. The supplement addresses exactly the governance gap: three-party joint authorization for the event as a whole, conflict-routing for three-way conflicts, and escalation paths for three-party disputes. The supplement must be jointly authorized by all three Selves — that three-way authorization is what the supplement exists to supply. The supplement does not replace the bilateral configs; it supplements them. Within the N = 3 event, bilateral conflicts follow the routing specified in the applicable bilateral config; three-way conflicts follow the routing specified in the supplement. This approach reuses existing governance infrastructure and limits the additional governance work to the gap. The cost is a supplement dependency: the supplement is a second governance instrument that must be maintained alongside the bilateral configs.

Neither approach is prescribed by the pattern. Both are valid architectural choices. The choice involves a governance trade-off: Approach A produces a cleaner single-instrument structure at higher upfront cost; Approach B reuses existing infrastructure with lower upfront cost but introduces supplement maintenance as an ongoing obligation.

### 3.3 N-Change Governance

The dynamic dimension of this composition pair is what happens when N changes.

Under Approach B, N-change handling is natural. When one Self exits an ongoing N = 3 event (returning to N = 2), the supplement is no longer needed: the bilateral config for the remaining pair governs the bilateral event. The bilateral configs are unaffected by the N-change. When a fourth Self joins (N = 4), the supplement must be updated to cover four-party joint authorization, four-way conflict routing, and four-party escalation; the bilateral configs are again unaffected. The supplement is N-specific; the bilateral configs are N-agnostic. N-change governance under Approach B is supplement-scoped.

Under Approach A, N-change handling requires replacing the multilateral standing config. When N changes from 3 to 2 (a Self exits), the trilateral config is no longer the appropriate governance instrument; a bilateral config governs the remaining pair. When N changes from 3 to 4 (a fourth Self joins), the trilateral config must be replaced with a quadrilateral config. The multilateral config encodes N as a fixed parameter; it does not degrade gracefully when N shifts. N-change governance under Approach A is full-config-replacement.

This asymmetry is a governance design consideration, not a defect in either approach. Organizations expecting frequent N changes may prefer the supplement architecture for its N-agnostic bilateral infrastructure. Organizations expecting stable N with high per-event governance clarity may prefer the multilateral config for its single-instrument structure.

---

## 4. Prior-Art Significance

The non-obvious insight — that bilateral standing configs do not compose automatically into N-ary governance — closes a specific adversarial gap. A claim to "using pre-authorized governance templates for multi-party AI coordination" might appear novel if the specific architectural analysis of what bilateral templates fail to cover at N > 2 scope were not in the prior art. This note establishes that analysis, and both valid approaches to closing the gap, as prior art.

More precisely: the identification of three-way conflict routing and three-way joint authorization as the specific governance dimensions absent from any collection of bilateral configs, the distinction between bilateral-config-scope and N-ary-event-scope as a structural rather than a degree-of-completeness distinction, the two-approach design space (multilateral config versus bilateral-plus-supplement), and the N-change governance asymmetry between the two approaches — all are established here as prior art at the architectural pattern level. Subsequent work may implement these approaches in specific systems, protocols, or platforms; those implementations stand on their own deployment claims. The architectural analysis is what this note places in the prior art.

---

## 5. Operational Test

For an N = 3 FAI event conducted under standing governance, an observer can apply the following three-part test to verify that the composition is validly instantiated:

**(a) Three-way joint authorization is present.** Either the governance instrument is a multilateral standing configuration jointly authorized by all three Selves (Approach A), or a bilateral-config-plus-supplement structure exists in which the supplement is jointly authorized by all three Selves (Approach B). Authorization by each pair separately, without a three-party authorization of a single shared governance instrument covering the N = 3 event, does not satisfy this requirement.

**(b) Three-way conflict routing is specified.** The governance framework explicitly addresses what happens when all three Selves' contributions to the same aspect diverge simultaneously. A governance framework that specifies only bilateral conflict routing — even for all three pairs — does not satisfy this requirement.

**(c) N-change governance is specified.** The governance framework specifies what happens when N changes: which instruments remain valid, which are retired, and which must be updated or replaced. Under Approach B, the supplement's N-specific scope and the bilateral configs' N-agnostic scope must be documented. Under Approach A, the replacement procedure for the multilateral config when N changes must be documented.

A governance framework that passes all three tests instantiates the Composition Pair 2 requirements. Failure on any one test indicates a governance gap at the standing-config / multi-Self boundary.

---

*End of Note D4.03.*
