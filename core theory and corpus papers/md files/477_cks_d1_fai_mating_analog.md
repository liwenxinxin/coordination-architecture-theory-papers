# FAI as the Inter-Self Analog of Paper 2 Mating

**Derivation Note D1.12 — CKS Theory Series, Phase D1**
**Series note #477**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2025
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the inter-Self coordination architecture introduced in "Inter-Self Coordination via Shared Substrate / Full Aspect Integration" (Li, April 2026), the third paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026) and "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026).

---

## Abstract

Full Aspect Integration (FAI), the canonical operation over the inter-Self shared substrate established in Paper 3 Claim 2, is not a novel architectural operation. It is structurally the same merge primitive as Paper 2's mating operation, applied at inter-Self rather than intra-Self scope. This note formalizes the structural parallel — same merge operation, same three pattern variants, same conflict-preservation requirement, same governance-authorization requirement — and the two structural differences that distinguish the inter-Self application: outcome type (FAI produces evolution outputs that feed into existing Paper 2 mechanisms; mating produces offspring entities that enter the deployment as new governed objects) and scope (FAI operates across multiple Selves' governance perimeters under joint authority; mating operates within one Self's governance perimeter under that Self's authority). The structural parallel closes the adversarial claim that FAI is a novel architectural operation; the structural differences explain why the inter-Self application does not create jointly-owned entities and why participating Selves retain full governance independence after an FAI event. This note closes the seven-note Claim 2 sub-commitment set (D1.06–D1.12); D1.13 begins Claim 3 sub-commitments (three-tier conflict handling).

---

## 1. Statement of D1.12

**D1.12:** FAI is the same merge primitive as Paper 2 mating, applied at inter-Self scope. The merge operation, the three pattern variants, the conflict-preservation requirement, and the governance-authorization requirement are structurally identical at both scopes. The differences — outcome type, scope of operation, authority structure, and treatment of participating entities — are the architectural consequences of extending the intra-Self merge primitive across organizational boundaries.

This is the seventh and final sub-commitment under Paper 3 Claim 2. The prior six sub-commitments (D1.06–D1.11) established: the aspect as the unit of exchange in FAI (D1.06), n-ary cardinality with a two-Self floor (D1.07), full merge as the architectural default at inter-Self scope (D1.08), the three pattern variants and their inter-Self instantiation (D1.09), the exchange boundary defined by Paper 2's instinct/reasoning separation (D1.10), and the three persistence loci for FAI outputs (D1.11). D1.12 establishes the relationship between FAI as a whole and the mating primitive Paper 2 introduced, completing the Claim 2 coverage.

---

## 2. Background: the mating primitive in Paper 2

Paper 2 establishes mating as a governed lifecycle operation combining two or more parent entities' governed content to produce offspring. The operation applies at cell scope, aspect scope, and Self scope within one Self's governance perimeter. Mating is a merge primitive: it takes the governed content — DNA-layer specifications, behavior rules, orchestration patterns — of multiple source entities and combines them according to one of three pattern variants, under governance authorization.

The three pattern variants Paper 2 defines:

**Full merge (union).** All contributing parent entities' governed content is combined into the offspring. The offspring carries the union of the contributing specifications. Conflicts that arise from combining content that specifies incompatible behaviors are registered as first-class conflict objects rather than silently resolved.

**Governance-curated merge (selective merge).** Governance selects which governed content from each contributing entity is included in the offspring. The selection is explicit and recorded; content excluded from the offspring is not lost from the parent's substrate but is not forwarded.

**Full merge with explicit provenance carry-over (lineage-preserved union).** All contributing content is combined, as in full merge, and explicit cross-lineage references are added to the offspring's substrate content, recording which content was inherited from which contributing entity. This variant supports downstream governance tracing of how contributed content shaped the offspring's behavior.

Mating in Paper 2 requires governance authorization: the lifecycle event must be authorized by the Self's governance authority before it proceeds. Conflicts produced by the merge are registered per Paper 1 Claim 2's conflict-preservation commitment, which applies recursively at all levels within a Self (Paper 2 D-series sub-commitments).

---

## 3. Structural parallels: what FAI and mating share

The structural parallel between FAI and mating is precise and exhaustive across four dimensions.

### 3.1 The merge operation

Both mating and FAI are merge operations over governed content. In mating, governed content from multiple parent entities — the DNA-layer specifications, orchestration rules, and behavior definitions those entities carry in their substrates — is combined to produce the output. In FAI, governed content from multiple Selves — the aspects those Selves contribute to the shared substrate, each aspect surfacing its constituent cells' DNA-layer and action-layer content — is combined within the shared substrate to produce the output.

The object being merged differs (parent entities' specifications vs. contributed aspects), and the target differs (offspring substrate vs. shared substrate), but the operation is the same: governed content from multiple sources is merged under architecture-specified rules into a shared output space. This is not analogy. The merge operation at inter-Self scope in FAI is the same architectural operation as the merge operation at intra-Self scope in mating, instantiated at a different coordination scope with different source objects.

### 3.2 Three pattern variants

FAI uses the same three pattern variants as mating, applied at inter-Self scope:

**Full merge.** All aspects contributed by participating Selves are merged within the shared substrate. This is the architectural default at inter-Self scope (D1.08). Conflicts arising from full merge of contributed content that specifies incompatible behavior are registered as first-class objects in the shared substrate (Paper 3 Claim 3, D1.13).

**Governance-curated merge (selective merge).** Governance — here, the joint governance authority of participating Selves — configures which aspects from each Self are included in the merge for a given FAI event. The selection is explicit and substrate-recorded. This variant is Paper 2's selective merge applied at inter-Self scope.

**Full merge with explicit provenance carry-over (lineage-preserved union).** All contributed aspects are merged, and explicit cross-perimeter provenance references are added to the shared substrate content, recording which content originated from which participating Self. This variant supports downstream governance tracing of how each Self's contribution shaped the evolution outputs. This is Paper 2's lineage-preserved union applied across the inter-Self perimeter.

The pattern variants are not novel in Paper 3. They are the same three patterns Paper 2 introduced, operating on a different coordination scope. Paper 3's contribution at the pattern-variant level is the architectural-default commitment: Paper 2 names no default among its three variants at intra-Self scope; Paper 3 names full merge as the default at inter-Self scope. The default commitment is the only pattern-level novelty; the variants themselves are inherited.

### 3.3 Conflict preservation

Both mating and FAI preserve conflicts as first-class objects. In mating, full merge or lineage-preserved union may produce conflicting specifications when the contributing entities have authored incompatible behavior rules. Paper 1 Claim 2's conflict-preservation commitment — conflicts are registered in the substrate, not silently resolved — applies at all levels within a Self (Paper 2's recursive application of A1.03). Mating events that produce conflicts register those conflicts in the offspring's substrate or in the parent Self's conflict registry.

In FAI, full merge of contributed aspects from multiple Selves may produce conflicting specifications across governance perimeters. Paper 3 Claim 3's three-tier conflict-handling mechanism (D1.13) governs what happens to those conflicts: they are preserved as first-class substrate state in the shared substrate (inheriting Paper 1's preservation commitment), managed through orchestration rules within the shared substrate where resolvable, and escalated to joint governance authority where unresolvable. The preservation commitment — the first tier — is the same commitment at inter-Self scope.

Conflict preservation is structurally identical across both operations. The handling mechanism differs at the escalation tier (inter-Self conflicts may escalate across governance perimeters; intra-Self conflicts escalate within one Self's authority), but the first-order commitment — conflicts are objects, not exceptions — is identical.

### 3.4 Governance authorization

Both mating and FAI require governance authorization before they proceed. In mating, the Self's governance authority must authorize the lifecycle event. In FAI, joint governance authority from the participating Selves' governance structures must authorize the event. The authorization requirement is structurally identical; the authority holding that authorization differs.

---

## 4. Structural differences: what distinguishes FAI from mating

The four structural differences between FAI and mating are not defects in the parallel — they are the architectural consequences of extending the merge primitive across organizational boundaries. Each difference is load-bearing.

### 4.1 Outcome type

This is the most significant structural difference.

**Mating produces offspring entities.** Offspring are new governed objects that enter the deployment as fully constituted architectural units. They have their own substrates, their own DNA and action layers, their own governance enrollment. After mating, the offspring exist independently in the deployment; they are not logically dependent on the parent entities for their continued operation. The parent entities may be closed as part of the mating lifecycle event (Paper 2's lifecycle closure commitment) or may continue operating — but the offspring are new, distinct governed entities.

**FAI produces evolution outputs.** Evolution outputs are not new governed entities. They are substrate content — DNA-layer and action-layer content — produced during the FAI event within the shared substrate, structured for ingestion into each participating Self's home substrate through Paper 2's existing evolution mechanisms (Paper 3 Claim 4, D1.17–D1.21). The evolution outputs dissolve with the shared substrate at FAI dissolution; what persists is the content each Self has ingested into its own home substrate.

This difference is architecturally significant for inter-organizational coordination. If FAI produced jointly-owned offspring entities, it would create governed objects with multiple organizational parents — a structurally novel entity type requiring new governance arrangements for ownership, lifecycle management, and authority allocation. By producing evolution outputs instead, FAI avoids creating jointly-owned entities entirely. Each participating Self ingests the outputs into its own home substrate under its own governance authority. The inter-Self coordination event produces no persistent shared object; it produces per-Self substrate enrichment that each Self owns independently.

This is precisely what makes FAI appropriate as the coordination primitive for inter-organizational AI architectures. Organizations that participate in a joint FAI event do not create a jointly-governed AI entity they must then manage across organizational lines. They exchange governed content, each Self evolves by ingesting the exchange outputs, and each Self retains full governance independence thereafter.

### 4.2 Scope of operation

Mating operates at intra-Self scope — within one Self's governance perimeter. The contributing entities (cells, aspects, or Self-level units) are all within the same home perimeter. The merge happens within a space governed by one governance authority.

FAI operates at inter-Self scope — across multiple Selves' governance perimeters. The shared substrate is a temporary perimeter constructed across home perimeters (Paper 3 Claim 1, D1.01–D1.05). The merge happens within a space that spans governance boundaries. This is a scope extension of the merge primitive, not a different primitive.

### 4.3 Authority structure

Mating is authorized and governed by one Self's governance authority. The governance authority of the Self in which mating occurs holds all three rights — inspect, modify, override — over the mating event and its outputs.

FAI is authorized and governed by joint authority. Each participating Self's governance authority holds inspect, modify, and override rights over the FAI event scoped to that Self's contributed content and to the evolution outputs that Self will ingest. The shared substrate itself is governed jointly. No single participating Self holds unilateral authority over the shared substrate or over another Self's evolution outputs.

Joint authority at inter-Self scope is a direct extension of the authority architecture Paper 1 and Paper 2 establish — the same three rights (inspect, modify, override), now held by two-or-more governance authorities over a shared scope — rather than a new authority concept.

### 4.4 Treatment of participating entities after the event

In mating, parent entities are lifecycle actors whose post-mating status is determined by governance: they may be closed as part of the mating event (a terminal lifecycle state) or may continue. The mating event is a lifecycle boundary for the parents.

In FAI, participating Selves are not consumed or bounded by the FAI event. A Self that participates in an FAI event retains its full governance independence, its full substrate, and its full lifecycle continuity after the event concludes. The FAI event is an evolution input for the participating Selves, not a lifecycle boundary. A Self can participate in multiple FAI events across its lifecycle, with different partners, without any implication of merger, closure, or transfer of governance authority.

---

## 5. The prior-art claim

The structural parallel in §3 establishes the prior-art coverage for FAI as a merge primitive. An adversary seeking to claim FAI as a novel architectural operation faces the following prior art:

The merge operation in FAI (§3.1) is the merge operation in Paper 2 mating applied at inter-Self scope. It is not novel.

The three pattern variants in FAI (§3.2) are the three pattern variants in Paper 2 mating applied at inter-Self scope. They are not novel. The only pattern-level novelty — the full-merge default commitment at inter-Self scope — is small and well-bounded; it does not support a claim that FAI's merge mechanism is a new architectural invention.

The conflict-preservation commitment in FAI (§3.3) is the conflict-preservation commitment from Paper 1 Claim 2, extended recursively through Paper 2 at intra-Self scope and applied at inter-Self scope in Paper 3. It is not novel.

The governance-authorization requirement in FAI (§3.4) is the governance-authorization requirement from Paper 2 mating, extended to joint authority at inter-Self scope. The joint authority extension is a scope extension of the authority architecture, not a new authority concept.

The adversarial space FAI must be defended against is therefore not "FAI duplicates mating" — that would collapse the inter-Self scope extension — but rather "FAI's merge mechanism is novel relative to mating." This note forecloses the latter claim. FAI is the mating primitive extended to inter-Self scope. The extension is architecturally significant (different outcome type, different scope, joint authority, non-consuming participation), but the primitive is inherited.

The corresponding adversarial failure mode in the opposite direction — "mating and FAI are the same operation and Paper 3 therefore adds nothing" — is foreclosed by the structural differences in §4. The inter-Self scope extension produces genuinely novel architectural commitments: the shared substrate as a temporary inter-Self perimeter (Paper 3 Claim 1), FAI's evolution-output outcome type rather than offspring creation, the four-locus evolution feed at dissolution (Paper 3 Claim 4), three-tier inter-Self conflict handling (Paper 3 Claim 3), and population-scale collective evolution (Paper 3 Claim 6). These are what the mating primitive produces when extended to the inter-Self scope; they are not present in Paper 2.

---

## 6. Operational test

Given governance records from an FAI event and a mating event, an observer with no architectural knowledge beyond what is recorded in the governance records should be able to identify:

**Three structural parallels (should be identifiable from records alone):**

1. *Merge operation:* Both records describe governed content from multiple sources being combined in a shared output space under architecture-specified merge rules, with the merge subject to governance authorization before execution.

2. *Three pattern variants:* Both records specify which pattern variant was selected (full merge, selective merge, or lineage-preserved union), with the selected variant recorded in substrate-accessible form prior to execution.

3. *Conflict preservation:* Both records show that conflicts produced by the merge event were registered as first-class objects — named entries in a conflict registry accessible to governance — rather than silently resolved or discarded.

**Two structural differences (should be identifiable from records alone):**

1. *Outcome type:* The mating record shows new governed entities created as outputs, with their own substrate entries, governance enrollment records, and lifecycle initialization events. The FAI record shows evolution outputs produced — substrate content structured for ingestion — with corresponding ingestion records at each participating Self's home substrate, but no new governed entity creation.

2. *Scope:* The mating record shows contributing entities and output entities all within one Self's governance perimeter, with authorization from one governance authority. The FAI record shows contributing Selves from two or more governance perimeters, with joint authorization recorded from each participating Self's governance authority, and the merge itself occurring within a shared substrate marked as spanning multiple home perimeters.

If an observer cannot make these identifications from governance records alone, the records are deficient. The operational test doubles as an accountability requirement: governance records for both event types must be sufficient to expose the structural parallel and the structural differences to inspection without additional architectural knowledge.

---

## 7. Closing the Claim 2 sub-commitment set

D1.12 is the seventh and final note in the Claim 2 sub-commitment set. The seven notes collectively cover the full architectural commitment of Paper 3 Claim 2:

- **D1.06** — The aspect as the unit of exchange: when a Self contributes to the shared substrate during an FAI event, the contribution is at aspect granularity, surfacing the aspect's constituent cells' DNA-layer and action-layer content.
- **D1.07** — N-ary cardinality: FAI supports two or more participating Selves; two-Self FAI is the simplest instance; the cardinality floor reflects Paper 3's scope addressing inter-Self cases (one-Self self-derived combination remains Paper 2's intra-Self territory).
- **D1.08** — Full-merge default: the architectural default for FAI is full merge of contributed aspects within the shared substrate; whether full merge is performed and which aspects each Self contributes is governance-configured per event.
- **D1.09** — Three pattern variants: FAI supports the same three pattern variants as Paper 2 mating (full merge, selective merge, lineage-preserved union), applied at inter-Self scope.
- **D1.10** — Exchange boundary: the exchange is bounded to substrate content per Paper 2's instinct/reasoning separation; DNA-layer content and action-layer content exchange through the shared substrate; LLM weights and instinct-layer content do not.
- **D1.11** — Three persistence loci: FAI outputs persist at three loci — within the shared substrate during the active FAI event, at each participating Self's home substrate after ingestion, and in the provenance records that record the event and its outputs.
- **D1.12** (this note) — FAI as mating analog: FAI is the same merge primitive as Paper 2 mating at inter-Self scope, with the same three pattern variants and the same conflict-preservation and governance-authorization requirements, distinguished by outcome type and scope.

Together, D1.06 through D1.12 establish the full prior-art and architectural coverage for Paper 3 Claim 2.

**D1.13 begins Claim 3 sub-commitments.** Claim 3 establishes the three-tier inter-Self conflict-handling mechanism: preserve conflicts as first-class substrate state in the shared substrate (inheriting Paper 1 Claim 2's preservation commitment); resolve conflicts of known classes via orchestration rules within the shared substrate (inheriting Paper 1 Claim 2's orchestration-governed resolution tier); escalate unresolvable conflicts to joint governance authority across the participating Selves' governance structures (the new tier at inter-Self scope). D1.13 begins this coverage with the preservation sub-commitment.

---

## References

Li, W. (April 2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* [Paper 1, CKS theory series.]

Li, W. (April 2026). *The Instinct/Reasoning Separation Outside the Model.* [Paper 2, CKS theory series.]

Li, W. (April 2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* [Paper 3, CKS theory series.]

---

*D1.12 — Note #477 in the CKS Derivation Note Series. Phase D1: Paper 3 claim-level sub-commitments.*
*Closes the Claim 2 sub-commitment set (D1.06–D1.12). D1.13 begins Claim 3.*
