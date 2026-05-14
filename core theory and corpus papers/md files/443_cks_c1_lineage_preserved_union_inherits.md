# Lineage-Preserved Union Inherits Paper 1's Path Retraceability

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

---

## Abstract

Paper 2 of the CKS theory series introduces three mating-pattern variants — union, selective merge, and lineage-preserved union — as governance-configured primitives for combining parental content across the DNA and action layers of AI Selves. This note formalizes the inheritance relationship between the third pattern and Paper 1: the lineage-preserved union pattern inherits Paper 1's path retraceability commitment (A1.07) and extends it to the entity scope, adding a new data structure — cross-lineage references — that makes the complete ancestry chains of both contributing parents independently traversable from the offspring's lineage record. The note shows what path retraceability's core properties — full-chain depth, the six provenance metadata fields, and plan-trace coupling — are preserved under the extension, and what is genuinely new in Paper 2: the branching structure of the provenance trail, the explicit-vs-implicit lineage distinction from the union pattern, and the dual-heritage auditability commitment. The note closes by summarizing all three mating-pattern inheritance edges (C1.12, C1.13, C1.14) as a completed triple, and states the prior-art significance of the full triple.

---

## 1. Position: the final mating-pattern inheritance edge

This note formalizes the third and final of three inheritance edges that together constitute the mating-pattern inheritance triple in the CKS cross-derivation series. The three edges map Paper 2's three mating patterns to their respective Paper 1 parent commitments:

- **C1.12**: Union inherits Paper 1's conflict preservation commitment. The union pattern keeps all DNA from both parents and commits to preserving merge-time conflicts as first-class substrate state — directly extending Paper 1's commitment that contradictions are addressable objects in the substrate.
- **C1.13**: Selective merge inherits Paper 1's write authority commitment. The selective merge pattern places humans or LLMs operating under human direction in the role of deciding what crosses the boundary from each parent — directly extending Paper 1's commitment that the authority to modify substrate content is preserved in human hands.
- **C1.14** (this note): Lineage-preserved union inherits Paper 1's path retraceability commitment. The lineage-preserved union pattern combines all parental DNA and additionally commits to placing explicit cross-lineage references in the offspring's lineage record — references that make the complete ancestry chains of both parents independently traversable from the offspring — directly extending Paper 1's commitment to full-chain provenance depth on all substrate content.

Each pattern in Paper 2 adds a distinct new architectural structure while drawing on a distinct prior commitment from Paper 1 as its governing mechanism. The triple together covers the full prior-art territory of mating as governed primitive: content combination, boundary governance, and provenance depth.

---

## 2. Paper 1 path retraceability as a depth commitment

Paper 1's path retraceability commitment (A1.07) is a structural property requirement on substrate content: every piece of content in a CKS substrate must carry sufficient provenance that the path back to its causal antecedents is reconstructable from the substrate alone, without consulting external logs, agent memory, or human recollection. The key property the commitment establishes is *depth*: not just one step back — not just "who wrote this and when" — but the full chain from any content back to the original inputs and governance decisions that produced it.

The commitment is operational because Paper 1 specifies what each piece of substrate content must carry. The six provenance metadata fields are: (a) writer attribution, distinguishing a human acting under preserved authority from an LLM operating under a named orchestration rule; (b) timestamp, making the path orderable over time; (c) antecedent reference, naming the prior substrate content the writer drew on; (d) rule reference for cell-mediated writes, naming the orchestration rule under which the write occurred; (e) rationale, where the accountability plan requires it; and (f) relationship to contradicting content, where applicable. With these six fields present on every content item, the path back to antecedents is a sequence of substrate reads; without them, the path runs through information the substrate does not carry and retraceability fails.

The depth commitment is also framed using the accountability vocabulary: every governance decision has a plan (authorization before the fact) and a trace (record after the fact), and the two are coupled. The plan specifies what the trace must capture; the trace records what the plan required. Path retraceability is the structural property the trace must have for the plan to be satisfied. Together, the six fields and the plan-trace coupling make any outcome in the system reconstructable from the substrate alone, at any point in the substrate's history.

---

## 3. Lineage-preserved union precisely

The lineage-preserved union pattern is the most provenance-intensive of Paper 2's three mating variants. Its definition has two components that must be held together to understand what it commits to.

**Component one — union DNA combination.** Like the union pattern, lineage-preserved union combines all DNA from both contributing parents into the offspring's substrate. Nothing is filtered or curated. The offspring carries the full DNA layers of both parents, together with any merge-time conflicts preserved as first-class substrate state per Paper 1's conflict-preservation commitment. In this respect, lineage-preserved union begins where union begins.

**Component two — explicit cross-lineage references.** Beyond the DNA combination, the lineage-preserved union pattern commits to placing explicit cross-lineage references in the offspring's lineage chain. These references are not parentage annotations on the mating event; they are traversable pointers into the *complete* lineage chains of both contributing parents. An observer following the offspring's lineage record can proceed through the offspring's own birth record and history, and additionally can follow either reference into the full historical chain of the corresponding parent, back to that parent's own origination. The lineage chain of the offspring branches: it connects to two separate parent chains, each of which is independently traversable in full.

The branching structure is a new data structure introduced in Paper 2. It is the specific architectural commitment that distinguishes lineage-preserved union from the simpler union pattern and from plain lineage tracking. It is also what makes the inheritance from Paper 1's path retraceability precise: the cross-lineage references carry the full-chain depth commitment forward, at mating time, for both parent lineages simultaneously.

---

## 4. What is preserved: path retraceability identity under the extension

Three properties of Paper 1's path retraceability commitment are preserved without modification under lineage-preserved union, and their preservation is what makes the inheritance relationship a genuine extension rather than a replacement.

**Full-chain depth.** Paper 1's depth commitment requires that any content in the substrate can be traced back through its complete chain of antecedents. Lineage-preserved union preserves this requirement and applies it to the offspring's lineage structure: the cross-lineage references placed in the offspring's lineage record point not to the parents' birth records alone but to their complete lineage chains. The depth that Paper 1 requires of substrate content generally, lineage-preserved union requires specifically of the mating event's provenance output. An observer can trace from any point in the offspring's history, through the cross-lineage references, back to the original births of both contributing parents. The chain does not stop at the mating event.

**Six provenance metadata fields.** The six fields Paper 1 specifies apply to all substrate content, and the lineage records that lineage-preserved union introduces are substrate content. The cross-lineage references themselves carry writer attribution, timestamp, antecedent reference, and rule reference — the same fields Paper 1 requires of every content item. The mating event's governance authorization (who authorized the lineage-preserved-union pattern, under which orchestration rule) is recorded per field (d); the resulting lineage record, including its cross-lineage references, constitutes the trace per field (c). There is no new provenance vocabulary; the six fields apply directly.

**Plan-trace coupling at mating time.** The governance decision to apply the lineage-preserved-union pattern is the plan: it authorizes in advance the specific content-combination behavior and the cross-lineage reference structure the pattern commits to. The offspring's lineage record — containing the combined DNA, the merge-time conflict records, and the cross-lineage references — is the trace: it records what the plan required. Plan and trace are coupled at the mating event in exactly the sense Paper 1's accountability vocabulary specifies. The mating decision is not simply an event that happened; it is a governance authorization with a corresponding substrate record, reconstructable from the substrate alone.

---

## 5. What is new: the cross-lineage reference structure and bifurcated provenance trail

While all three properties above are preserved, lineage-preserved union introduces three genuinely new features that represent Paper 2's extension of Paper 1's scope.

**Cross-lineage references as new data structure.** Paper 1's path retraceability applies to substrate content generally: every content item has a path back through its antecedents. Paper 1 does not introduce or require any specific data structure for lineage at the entity level; the provenance metadata fields are properties of content items, and the retraceable paths run through content. The lineage-preserved union pattern introduces a named data structure — cross-lineage references — that explicitly connects the offspring's lineage chain to two separate parent chains as a governance commitment. This structure is new in Paper 2. It is not derivable from Paper 1's provenance field requirements alone; it is an entity-scope extension that applies the depth commitment to the mating operation as an architectural primitive.

**Bifurcated provenance trail.** Paper 1's path retraceability is single-chain: any substrate content has one provenance path, running from the content back through its antecedents to origination. The lineage-preserved union pattern introduces a two-path ancestry structure at the offspring level. An observer following the offspring's lineage does not simply retrace one chain; the lineage record branches, and both branches are fully traversable. The observer can independently verify the complete history of either parent through the offspring's own lineage record. This bifurcation is not a relaxation of Paper 1's depth requirement — it is that requirement applied twice over, once for each parent's chain — but the two-path structure itself is new.

**Explicit vs. implicit lineage.** This is the distinction that separates lineage-preserved union from the union pattern at the architectural level. Union (C1.12) also combines parental content and records the mating event. The mating event in union implicitly captures parentage: an observer who reads the mating event record can determine which parents contributed. But union does not commit to placing *traversable pointers* into the full parent chains within the offspring's lineage record. The parentage is recorded; the ancestry trails are not made independently navigable from the offspring. Lineage-preserved union adds the explicit traversable references as a governance commitment. The distinction matters for auditability: implicit parentage answers "where did this come from?" for the mating event; explicit cross-lineage references answer "what is the complete independent history of each contributor?" for any audit that needs to reach back through either parent's full chain from the offspring's own records.

The use case Paper 2 targets with this pattern is precisely the case where the offspring's dual heritage is architecturally significant and needs to be independently auditable — where an auditor must be able to verify the complete provenance of each parent lineage from the offspring's records alone, without locating and independently traversing each parent separately.

---

## 6. Operational test

A governance system implements the lineage-preserved union pattern as an extension of Paper 1's path retraceability if and only if all of the following are true for an offspring produced under this pattern:

1. The offspring's lineage record contains explicit cross-lineage references to both contributing parent lineage chains, as substrate content carrying the six provenance metadata fields Paper 1 specifies.
2. An observer starting at the offspring's birth record can follow the cross-lineage reference for Parent A through that parent's complete lineage chain to Parent A's own origination, reading only substrate content at each step.
3. The same observer can independently follow the cross-lineage reference for Parent B through that parent's complete lineage chain to Parent B's own origination, reading only substrate content at each step.
4. Both traversals in (2) and (3) are performable from the offspring's records alone, without locating the parent cells separately or consulting records external to the substrate.
5. The governance authorization for applying the lineage-preserved-union pattern is present in the offspring's lineage record as a plan, and the cross-lineage references and combined DNA together constitute the corresponding trace, coupled per Paper 1's accountability vocabulary.

A system in which the parentage of a mating event is recorded in the mating event record but the full parent chains are not traversable from the offspring's lineage record satisfies union-pattern provenance, not lineage-preserved-union provenance. Condition (4) is the operational discriminator: the two ancestry trails must be navigable from the offspring's own substrate content.

---

## 7. Closing the three-mating-pattern inheritance triple

The three inheritance edges in the mating-pattern triple — C1.12, C1.13, and C1.14 — collectively formalize the prior-art territory of Paper 2's mating mechanism as a governed lifecycle primitive derived from Paper 1's six architectural commitments. The triple is now complete. Its structure is as follows.

**C1.12 — Union inherits conflict preservation.** The union pattern combines all parental DNA and commits to preserving merge-time conflicts as first-class substrate state in the offspring. The primary Paper 1 commitment this extends is conflict preservation: just as Paper 1 requires contradictions encountered during AI-mediated coordination to be retained as addressable substrate objects with identity and provenance, union extends that requirement to the merge-time conflicts that arise when two full parental substrates are combined. The governance mechanism Paper 1 introduces — conflicts as first-class substrate state rather than resolved-and-discarded artifacts — is the mechanism union operates under at mating time.

**C1.13 — Selective merge inherits write authority.** The selective merge pattern places humans or LLMs under human direction in the role of deciding what crosses the boundary from each parent into the offspring. The primary Paper 1 commitment this extends is write authority: the human-governed architecture's requirement that the authority to modify and populate substrate content is preserved in human hands. Selective merge does not just record that humans chose; it makes the curation rules themselves substrate content under human authority, extending Paper 1's governance-over-content-population commitment to the mating operation.

**C1.14 — Lineage-preserved union inherits path retraceability.** The lineage-preserved union pattern combines all parental DNA and additionally commits to placing explicit cross-lineage references in the offspring's lineage record, making the complete ancestry chains of both parents independently traversable from the offspring. The primary Paper 1 commitment this extends is path retraceability: the full-chain depth requirement on all substrate content, the six provenance metadata fields, and the plan-trace coupling of the accountability vocabulary. The new architectural structure — cross-lineage references creating a bifurcated provenance trail — is Paper 1's depth requirement applied at entity scope to the mating primitive, extended to both parent chains simultaneously.

**What the triple covers as prior-art territory.** Each pattern inherits a different Paper 1 commitment as its governing mechanism, and each adds a distinct structural element new in Paper 2. Together, the triple formalizes three independently claimable architectural combinations: content combination under conflict governance (union + conflict preservation), boundary governance with authority preservation (selective merge + write authority), and deep-provenance combination under bifurcated lineage structure (lineage-preserved union + path retraceability). Any claim to novelty in any of these three combinations — in the governance of merge-time conflicts as inherited from a substrate commitment, in the placement of curation authority as an extension of write-authority governance, or in the use of explicit cross-lineage references to make dual-parent ancestry trails independently traversable — falls within the prior-art territory the triple establishes.

---

## 8. Prior-art significance

This note forecloses three categories of adversarial novelty claims.

**First**, it forecloses claims that maintaining full cross-lineage references from offspring to both parent chains is novel relative to Paper 1's path retraceability. The cross-lineage references are Paper 1's depth commitment applied at entity scope to the mating primitive. The structure is new; the governing commitment is not. Any claim to novelty in the specific architecture of cross-lineage references as a provenance mechanism must contend with the prior art established by the combination of Paper 1's path retraceability requirement and Paper 2's formalization of it as a mating-time data structure.

**Second**, it forecloses claims that bifurcated provenance trails in entity lineage are novel. The two-path ancestry structure introduced by lineage-preserved union applies Paper 1's single-chain depth requirement twice over — once per parent chain — at the mating event. The bifurcation is architecturally new in Paper 2, but it is explicitly derived from a prior commitment, not introduced without prior-art grounding.

**Third**, it forecloses claims that the lineage-preserved union pattern introduces governance objects beyond Paper 1's scope. Every element of the pattern — the cross-lineage references, the mating event plan-trace coupling, the six provenance fields carried by lineage records, the full-chain depth requirement on the resulting ancestry trails — is traceable to Paper 1's A1.07 commitment and the accountability vocabulary Paper 1 imports. No element of the pattern requires a governance primitive not already established in Paper 1.

Together with C1.12 and C1.13, this note establishes the full three-pattern mating inheritance triple as prior art. The triple is published as three sequentially issued derivation notes in the CKS defensive publication series, with each note formalizing a single inheritance edge and together covering the governance territory of mating as a lifecycle primitive in Paper 2's architecture.

---

*This note is part of the CKS Derivation Notes series (Wenxin Li, 2026). License: CC BY 4.0.*
