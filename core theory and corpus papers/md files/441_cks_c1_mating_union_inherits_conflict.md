# Mating-Union Pattern Inherits Paper 1's Conflict Preservation

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
**Series:** CKS Derivation Notes — Series C, Note C1.12 (#441)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to establish, as explicit prior art, that Paper 2's union mating pattern is a direct application of Paper 1's conflict-preservation commitment at entity-DNA scope, and that the conflict registry populated at the moment of union-birth inherits its first-class structure from Paper 1 Claim 2 (A0.02).

---

## Abstract

Paper 2 of the CKS theory series introduces three mating pattern variants — union, selective merge, and lineage-preserved union — as governed lifecycle primitives over entity content combination. The union pattern commits to retaining all DNA specifications from both parent entities in the offspring, with all conflicts that arise from combining both parents' specifications registered as first-class substrate state at birth. This note establishes the inheritance edge: the union pattern's core architectural commitment is an entity-scope application of Paper 1 Claim 2 (A0.02), which commits to conflict preservation as a first-class architectural property at cell-coordination scope. The four load-bearing properties of Paper 1's conflict preservation — both sides retained, first-class registration, not automatically resolved, and attributed provenance — each carry through intact into the union pattern's behavior at entity birth. What is new in Paper 2 is the scope of application (entity-DNA rather than cell-coordination), the governance artifact that results (a conflict registry populated at birth), and the deliberate-choice character of union mating as a governance decision to accept maximum conflict density at birth. This note also introduces the three-mating-pattern inheritance triple (C1.12, C1.13, C1.14), in which each of the three mating patterns inherits from a distinct Paper 1 commitment.

---

## 1. The inheritance edge stated

**C1.12 Inheritance claim:** Paper 2's union mating pattern (Paper 2, §6.3, Claim 3) inherits from Paper 1's conflict preservation commitment (Paper 1, §5, Claim 2 / A0.02). The union pattern's defining architectural commitment — retain all specifications from both parent entities and register all conflicts as first-class substrate state at birth — is an entity-scope instantiation of Paper 1's commitment that conflicts encountered in governed coordination are preserved in the substrate as first-class addressable objects with their own identity and provenance.

The relationship is inheritance, not independent invention. The union pattern does not introduce a fresh conflict-handling philosophy; it applies Paper 1's existing conflict-preservation architecture at a new scope — the moment of entity birth under union combination — and extends it with a new governance artifact, the conflict registry, whose entries are structurally identical to the first-class conflict objects Paper 1 commits to.

---

## 2. What the union mating pattern produces

The union mating pattern is one of three pattern variants available when two entities combine to produce an offspring. Its defining commitment is maximally inclusive: all DNA-layer specifications from both parents are combined into the offspring's DNA. Neither parent's rules are discarded, filtered, or weighted at combination time. The offspring is born carrying the complete governing specification of each parent.

Because two entities that governed the same operational territory may have done so with different, potentially incompatible rules, combining their full DNA necessarily produces an offspring whose DNA may contain conflicts — rules that contradict each other or assert incompatible defaults over the same domain. This is not a failure mode; it is the expected output of union combination. The union pattern is chosen precisely because retaining all content from both parents is the governance goal, even at the cost of introducing conflicts the offspring must carry.

The architectural commitment at the moment of birth is therefore two-part. First, all parent DNA is retained in the offspring's substrate — both sides of every potential conflict are present. Second, the conflicts that arise from the combination are registered in the offspring's conflict registry at birth. The offspring is born with (a) a complete DNA containing all parent specifications and (b) a populated conflict registry recording all conflicts that resulted from combining those specifications, with entries carrying provenance identifying which parent contributed which conflicting rule.

Subsequent governance addresses the registered conflicts through directed selection events — governed choices that resolve specific conflicts by selecting one rule, combining both, or introducing a new rule. The conflicts are not auto-collapsed at mating time. The offspring begins its operational life with all parent DNA intact and a known, attributed set of conflicts that governance must address.

---

## 3. Conflict preservation identity preserved

Paper 1 Claim 2 (A0.02) commits to conflict preservation as a first-class architectural property at cell-coordination scope. That commitment has four load-bearing properties. Each carries through intact into the union pattern's behavior at entity birth.

**Both sides retained.** Paper 1 commits that when two governed specifications conflict at cell scope, both sides are preserved in the substrate — neither is silently discarded, neither is overridden without governance decision. The union pattern applies this property at entity-DNA scope: both conflicting rules from each parent are present in the offspring's DNA. The property holds at the larger scope without modification. This is the load-bearing inheritance. Without it, the union pattern would degenerate into an undeclared partial merge in which one parent's specification quietly wins at combination time.

**First-class registration.** Paper 1 commits that conflicts are registered as first-class objects in the substrate with their own identity — they are addressable, inspectable substrate state, not ephemeral markers or error conditions. The union pattern's conflict registry entries at birth are first-class substrate objects with their own identity. They are persistent across sessions, addressable after birth, and carry the same structural status as any other substrate content. The first-class character of Paper 1's conflict objects is not diluted at entity scope.

**Not automatically resolved.** Paper 1 commits that conflicts are not auto-resolved at the moment of detection. The detect-and-preserve posture is the architectural default; resolution happens through subsequent governed action, not through default arbitration. The union pattern applies this exactly: conflicts are registered at birth and remain unresolved until governance acts. The offspring is not required to resolve conflicts before it can operate. Deferral is a terminal recorded outcome, not a transitional state to be cleaned up.

**Attributed provenance.** Paper 1 commits that conflict objects carry attribution — identity information that makes the source of each conflicting entry traceable. The union pattern's conflict registry entries carry provenance identifying which parent contributed which conflicting rule. Attribution is not a Paper 2 innovation; it is a property Paper 1 commits to for first-class conflict objects, applied at the point of entity birth.

The four properties together constitute what Paper 1 calls "conflict preservation as first-class architectural property." All four hold in the union pattern's behavior at entity birth. The inheritance is complete and without dilution.

---

## 4. What is new in Paper 2

Inheritance without contribution would be mere citation, not an architectural extension. The union pattern carries three items of new content beyond what Paper 1 commits to, each of which depends on the inherited foundation but is not contained in it.

**Entity-scope application.** Paper 1's conflict preservation operates at cell-coordination scope: the context is conflicts between specifications encountered during AI-mediated coordination within a cell. The union pattern applies the same architectural commitment at entity-DNA scope: the context is conflicts between two entities' entire governing specifications at the moment those specifications are combined to produce an offspring. The scope extension is real — entity DNA is the aggregate of all orchestration rules, behavioral specifications, and relational definitions that govern an entity's operation across all its cells and aspects. Combining two entities' full DNA is a larger-scope operation than combining two cell-level coordination entries. The conflict-preservation architecture handles both scopes through the same commitment, but the entity-scope application is new to Paper 2.

**Conflict registry at birth as governance artifact.** Paper 1 commits to conflicts as first-class substrate state. Paper 2 introduces a specific governance artifact that instantiates this commitment at the moment of entity creation: the conflict registry, populated at birth by the union combination operation. The registry is not merely a list of detected conflicts; it is a governance artifact that defines the set of open governance questions the new entity carries from its first moment of existence. The entity is born with known, attributed, recorded conflicts that governance must address through subsequent directed selection. The conflict registry at birth is a new architectural primitive that Paper 1's conflict-preservation commitment made structurally possible but did not itself introduce.

**Union as deliberate conflict-maximizing governance choice.** Paper 1 specifies the conflict-preservation architecture; it does not specify a combination operation that governance can deliberately choose in order to maximize the conflicts inherited by an offspring. The union pattern is precisely that: a governance-selectable combination primitive whose distinguishing property is that it preserves all conflicts from both parents, accepting maximum conflict density at birth as the price of complete content retention. Governance chooses union knowing it will produce a populated conflict registry at birth. This deliberate-choice character — the explicit willingness to begin with maximum conflict density — is a new governance framing that the inherited conflict-preservation architecture enables but does not itself constitute.

---

## 5. The three-mating-pattern inheritance triple

The union mating pattern is one of three pattern variants Paper 2 introduces. The other two are selective merge and lineage-preserved union. Each pattern inherits from a distinct Paper 1 commitment, producing a triple of inheritance edges:

**C1.12 (this note) — Union ⊃ conflict preservation (A0.02).** The union pattern's all-in combination generates a conflict registry at birth; the entries inherit their first-class structure from Paper 1's conflict-preservation commitment. The load-bearing property is both-sides-retained: no parent specification is silently discarded.

**C1.13 (forthcoming) — Selective merge ⊃ human-governed write authority.** The selective-merge pattern delegates to governance — humans or agents under human direction — the authority to determine which rules from each parent cross the boundary into the offspring. The curation rules themselves are substrate content under human authority. This inherits Paper 1's human-governed write authority: the authority over which content enters the substrate belongs to humans, and that authority extends to the combination operation at entity birth.

**C1.14 (forthcoming) — Lineage-preserved union ⊃ path retraceability.** The lineage-preserved union pattern retains pointers to parent entities in the offspring's substrate, so that every element of the offspring's DNA has traceable derivation back to its source. This inherits Paper 1's path retraceability commitment: decisions and substrate content remain linkable to their derivation history through the substrate itself, not through external annotation.

Together, C1.12 through C1.14 establish that each mating pattern variant in Paper 2 is architecturally grounded in a specific Paper 1 commitment, and that the three-pattern design is not a free-standing invention but a governed set of options each of which inherits without redefense from the Paper 1 architecture it extends.

---

## 6. Prior-art significance

This note forecloses two categories of adversarial claim.

**Category A:** A claim that combining entity DNA specifications while preserving all conflicts as first-class substrate state is novel relative to Paper 1's conflict preservation. This note establishes that the union pattern's behavior is a direct entity-scope application of Paper 1 Claim 2 (A0.02). The all-in combination that generates a populated conflict registry at birth is not independent of Paper 1's conflict-preservation architecture; it is that architecture applied at entity-DNA scope. No party can claim novelty for the combination behavior without engaging the inheritance relationship this note establishes.

**Category B:** A claim that a conflict registry populated at entity birth — recording all conflicts arising from combining two entities' governing specifications, with both sides retained and neither auto-resolved — is novel relative to Paper 1's first-class conflict architecture. This note establishes that the conflict registry entries inherit their four structural properties (both-sides-retained, first-class registration, not auto-resolved, attributed provenance) directly from Paper 1 Claim 2. The registry as a governance artifact at entity scope is new to Paper 2; the structural character of its entries is inherited from Paper 1. No party can claim novelty for the registry's entry structure without engaging this inheritance.

Both categories of claim now face the public prior-art record of the Paper 1 → Paper 2 inheritance chain established in the CKS derivation note series.

---

## 7. Operational test

The inheritance claim in this note is architecturally testable. For any offspring entity produced by a union mating operation, the following operational test checks whether the conflict-preservation identity is preserved:

**Test C1.12 — Conflict registry completeness and structure at birth:**

1. **Both sides retained:** Enumerate all DNA-layer specifications contributed by Parent A and all DNA-layer specifications contributed by Parent B. Verify that the offspring's DNA contains all specifications from both parents. If any rule from either parent is absent from the offspring's DNA without an explicit governance decision recorded in the substrate, the union pattern's both-sides-retained commitment is violated.

2. **First-class registration:** For each pair of conflicting rules identified in the offspring's DNA — rules from different parents that contradict each other or assert incompatible behavior over the same operational domain — verify that a corresponding entry exists in the offspring's conflict registry at birth. If a conflict between parent rules exists in the DNA but has no registry entry, the first-class registration requirement is violated.

3. **Not auto-resolved:** Inspect the conflict registry entries as they exist at the moment of birth, before any directed selection event. Verify that each entry records the conflict in its unresolved state — both conflicting rules present, no automatic winner selected, no silent override. If any conflict is found to have been auto-resolved at combination time without a recorded governance decision, the not-auto-resolved commitment is violated.

4. **Attributed provenance:** For each conflict registry entry, verify that the entry records which parent contributed each of the two conflicting rules. If provenance is absent from any conflict registry entry, the attributed provenance requirement is violated.

A system passes Test C1.12 if and only if all four checks are satisfied for every union-mating birth event in the system's substrate history. A system that passes Test C1.12 instantiates the conflict-preservation identity inherited from Paper 1 Claim 2 at entity-DNA scope.

---

## 8. Summary

The union mating pattern in Paper 2 is an entity-scope application of Paper 1's conflict preservation as first-class architectural property. The four load-bearing properties of Paper 1 Claim 2 (A0.02) — both sides retained, first-class registration, not automatically resolved, attributed provenance — each carry through intact into the union pattern's behavior at entity birth. What is new in Paper 2 is the entity-DNA scope, the conflict registry at birth as a governance artifact, and union as a deliberate governance choice to accept maximum conflict density at birth in exchange for complete content retention. The inheritance edge is C1.12, the first of three mating-pattern inheritance notes (C1.12 union/C1.13 selective merge/C1.14 lineage-preserved union) that together establish that each of Paper 2's three mating pattern variants inherits from a distinct Paper 1 architectural commitment.

---

*End of Note C1.12 (#441)*
