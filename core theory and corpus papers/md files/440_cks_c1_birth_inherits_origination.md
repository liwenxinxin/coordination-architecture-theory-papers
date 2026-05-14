# Entity Birth Inherits Paper 1's Substrate Origination Pattern

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series. It does not introduce new axioms. Its sole contribution is to articulate, in precise form, how Paper 2's formalization of entity birth as a governed lifecycle primitive inherits from — rather than independently invents — the substrate origination pattern established in Paper 1, so that downstream work has a clear record of what was extended and what was added.

---

## Abstract

Paper 2 formalizes *birth* as a governed lifecycle primitive: a new entity (cell, aspect, or Self) comes into governed existence through a human-authorized birth event that produces a birth record, an initial DNA specification, a level determination, and a lineage anchor. Paper 1, predating this formalization, already committed to three properties that jointly define what it means for a governed substrate object to *originate*: authorized creation (from its human-governed authority commitment), attributed record (from its path retraceability commitment), and provenance from origination (from its accountability vocabulary). This note demonstrates that Paper 2's entity birth inherits all three Paper 1 origination-pattern commitments, and identifies what is genuinely new in Paper 2: entity-level naming, level determination at birth, initial DNA specification, lineage anchoring as a chain structure, and birth verification. The note also provides an operational test for verifying that the three inherited commitments hold independently of the Paper 2 additions, and previews the lifecycle inheritance triple (birth, mating variants, death) that Series C notes C1.11, C1.12, and C1.15 collectively establish.

---

## 1. The inheritance edge this note states

C1.11 in the CKS cross-derivation series formalizes the following inheritance relationship:

> **Paper 2 entity birth ⊃ Paper 1 substrate origination patterns**

The symbol ⊃ means that Paper 2's entity birth commitment strictly contains Paper 1's substrate origination patterns: everything Paper 1 committed to for substrate content origination is preserved at entity birth, and Paper 2 adds further structure beyond what Paper 1 committed to. The relationship is inheritance with extension, not replacement, and not independent invention.

Stating the edge precisely matters because the transition from Paper 1 to Paper 2 could superficially appear to introduce an entirely new governance concept. Paper 1 governs *substrate content*: arbitrary structured representations the substrate carries. Paper 2 governs *named entities* — cells, aspects, Selves — each of which comes into existence through a lifecycle event called birth. The vocabulary shift from "substrate content origination" to "entity birth" is real. What this note shows is that the underlying governance pattern is the same in both cases, extended and enriched in Paper 2 but not replaced.

---

## 2. Paper 1's substrate origination pattern: three commitments

Paper 1 does not use the word "birth." It governs the origin of substrate content through three commitments that together constitute what this note calls the *substrate origination pattern*.

**Commitment 1: Authorized creation (from Paper 1's human-governed authority).** Paper 1 commits to human-governed authority over substrate content and orchestration rules (§3, §4). This commitment means, at the moment any substrate content comes into existence, that its entry into the substrate requires human authorization. No substrate content appears without governance involvement: either humans author it directly, or LLMs operating under human direction produce it subject to human override. The authority is not a post-hoc audit right; it applies at the moment of origination. A piece of substrate content that entered the system without human governance authorization is not CKS-compliant content, regardless of what it contains.

**Commitment 2: Attributed record (from Paper 1's path retraceability commitment).** Paper 1 imports the path retraceability vocabulary from Rajabi and Kafaie (2022) and commits to it for all substrate content (§3.1). Path retraceability requires that every piece of substrate content carry sufficient provenance that its causal antecedents can be reconstructed from substrate content alone. The provenance fields include writer attribution, timestamp, orchestration rule reference (for cell-mediated writes), and antecedent reference. These fields are not optional metadata appended after the fact; they are required from the moment the content is written. When substrate content originates, it originates *as an attributed record*, not as an anonymous entry to which attribution is later assigned. The attribution is part of the origin event.

**Commitment 3: Provenance from origination (from Paper 1's accountability vocabulary).** Paper 1 imports the accountability plan / accountability trace distinction from Naja et al. (2021) and commits to both halves (§3.1). The accountability plan is what the substrate schema and orchestration rules specify must be captured; the accountability trace is what actually accumulates as substrate content. For the plan-and-trace contract to hold, the trace must begin at the moment of origination. A piece of substrate content that enters the system without being part of the accountable trace from its first moment would leave a gap in the trace — a period during which the content existed but was not governed. Paper 1's accountability vocabulary forecloses this by requiring that provenance tracking begin at origination, not at some later point after the content has been in use.

These three commitments are not independent: they reinforce each other. Authorized creation without attributed record would produce governance-authorized content with no auditable account of its authorization. Attributed record without provenance from origination would produce well-provenienced content whose early history is missing. Provenance from origination without authorized creation would produce a complete trace of content whose entry into the system was ungoverned. The three together — and only together — constitute the origination pattern Paper 1 commits to.

---

## 3. Paper 2 entity birth: what the formalization adds

Paper 2 (§6, Claim 3) formalizes birth as a governed lifecycle primitive. Birth is the creation of a new cell, aspect, or Self under human governance. The formalization specifies that a birth event produces: (a) a birth record recorded in the substrate, (b) an initial DNA specification governing the entity's behavior, (c) a level determination placing the entity at cell, aspect, or Self scope, and (d) a lineage anchor establishing the entity's position in a lineage chain.

Paper 2 also commits that origination "may be performed by humans directly or by LLMs operating under human direction" and that "the architectural commitment is governance, not labor" (§6.1). This positions Paper 2's birth commitment as a lifecycle governance commitment, parallel to Paper 1's substrate governance commitment, and distinguishes both from labor assignments.

What Paper 2 adds beyond Paper 1's origination pattern falls into five categories.

**Entity-level naming.** Paper 1 governed *substrate content* as the unit of governance. Paper 2 governs *named entities* — a cell named with an identity, an aspect named in relation to the Selves it composes, a Self with a governed identity across its lifecycle. The birth event brings a named entity into existence, not merely a piece of content. The named entity is the subject of a lifecycle; substrate content, in Paper 1, had no lifecycle concept attached to it.

**Level determination at birth.** The entity's structural level — cell, aspect, or Self — is determined at birth and recorded as part of the birth record. This level determination has no counterpart in Paper 1. Paper 1's substrate content is not typed by structural level; it is structured by schema and orchestration rules. Paper 2's three-level architecture (Claim 2, §5) introduces a structural taxonomy that applies from the moment of birth.

**Initial DNA specification at birth.** The entity begins existence with an authored DNA specification — a substrate-resident specification of its behavioral and structural identity. This is more than provenance metadata. A birth record under Paper 1's origination pattern carries attribution, timestamp, and antecedent reference; it records what happened. A DNA specification at birth governs what the entity will do going forward. The entity does not merely have a record; it has a behavioral specification from its first moment of existence.

**Lineage anchor as chain structure.** Paper 1 committed to provenance from origination as a property of individual substrate objects. Paper 2's lineage anchor at birth establishes not just provenance for the birth record itself, but the starting point of a *chain* that will accumulate mating history and directed selection history as the entity ages. The chain structure is genuinely new in Paper 2. The provenance-from-start principle is inherited from Paper 1; what is new is that the "start" in Paper 2 is the anchor of a growing lineage chain, not merely the provenance timestamp of a static piece of content.

**Birth verification.** Paper 2 commits to a verification step at birth confirming the entity satisfies its level's governance requirements before it begins operation. This is a new governance checkpoint not present in Paper 1. Paper 1's authorized creation commits that content does not enter the system without human governance authorization; Paper 2's birth verification adds a structural confirmation step — the entity must demonstrably satisfy the requirements of its level before it is active. The checkpoint closes a gap that Paper 1 did not need to close, because Paper 1 had no structural levels whose satisfaction could be verified.

---

## 4. What is preserved: the inheritance in detail

Each of Paper 1's three origination-pattern commitments travels intact into Paper 2 entity birth.

**Authorized creation at entity birth.** Paper 2 commits explicitly that birth occurs "under human governance" and that the architectural commitment is governance, not labor. An entity whose birth was not authorized under human governance is not a CKS-governed entity. This directly inherits Paper 1's commitment that no substrate content enters the system without governance involvement. The subject has changed — from substrate content to named entity — but the governance requirement at origination is the same.

**Attributed record at entity birth.** The birth record is substrate content. As substrate content, it carries the six provenance fields Paper 1's path retraceability commitment requires: writer attribution, timestamp, orchestration rule reference, antecedent reference, and (where the accountability plan calls for them) rationale and contradiction relationships. The birth record is not exempt from the path retraceability commitment because it is a lifecycle record rather than a task record. It is a piece of substrate content, and Paper 1's commitment applies to all substrate content.

**Provenance from origination at entity birth.** The lineage anchor established at birth is the entity's first contribution to the accountability trace. The trace does not begin at the entity's second action, or when the entity first performs a task; it begins at birth. The accountability plan — specified by the substrate schema and orchestration rules — requires that the trace be complete from origination. The birth record, carrying the lineage anchor, satisfies that requirement. Provenance tracking begins at the entity's first moment of governed existence.

**Substrate as source of truth at birth.** Paper 1's substrate-as-source-of-truth commitment holds for the birth record: the birth record in the substrate is the authoritative record of the entity's existence. An entity for which no birth record exists in the substrate is not a CKS-governed entity, regardless of any other evidence of its existence. The substrate is what certifies existence; the birth record is the certification.

---

## 5. Operational test: verifying the three inherited commitments independently

The following operational test establishes whether the three Paper 1 origination-pattern commitments hold for a given entity birth record, independently of the Paper 2 additions. An observer with access to the substrate and its governance documentation applies the test to any entity birth record B.

**Test 1 (Authorized creation):** Is there substrate-resident evidence that B's creation was authorized under human governance? Specifically: (a) does B carry writer attribution identifying a human acting under governance authority, or an LLM operating under a named orchestration rule? (b) does the orchestration rule under which B was created authorize entity birth events? (c) is there no substrate evidence that B entered the system through a path that bypassed human governance? If all three are satisfied, the authorized-creation commitment holds for B.

**Test 2 (Attributed record):** Does B carry the six provenance fields required by Paper 1's path retraceability commitment — writer attribution, timestamp, orchestration rule reference (if cell-mediated), antecedent reference (if any), rationale (where the accountability plan requires it), and contradiction relationships (where applicable)? Can an observer reconstruct the path from B back to its antecedents by reading substrate content alone, without consulting external logs, agent memory, or human recollection? If yes, the attributed-record commitment holds for B.

**Test 3 (Provenance from origination):** Is B the first entry in the entity's accountability trace — meaning the trace begins at birth rather than at some later point? Does the lineage anchor established by B represent the entity's position in the accountable trace from its first moment of governed existence? Is there no gap between the entity's creation and the beginning of its trace? If yes, the provenance-from-origination commitment holds for B.

Each test applies to the birth record *as a piece of substrate content*, independently of the Paper 2 additions (level determination, DNA specification, lineage chain structure, birth verification). A system can pass all three tests and lack the Paper 2 additions — such a system satisfies Paper 1's origination pattern at the entity level but does not yet implement Paper 2's full entity birth formalization. Conversely, a system that has level determination, DNA specification, and a lineage chain structure at birth but fails any of Tests 1–3 inherits none of Paper 1's origination pattern commitments — it has Paper 2's additions without the foundation those additions extend.

---

## 6. Preview: the lifecycle inheritance triple

C1.11 is the first of three Series C notes that together establish the lifecycle inheritance triple.

C1.12 will address mating variants. Paper 2's three mating patterns each inherit from a specific Paper 1 commitment: union (keep everything from both parents, preserve all conflicts) inherits from Paper 1's conflict preservation commitment (Claim 3); selective merge (pre-curated combination under human or LLM direction) inherits from Paper 1's human-governed write authority; lineage-preserved union (offspring carries pointers to parents for full provenance traceability) inherits from Paper 1's path retraceability commitment. The three mating variants are not independent inventions; they are three modes of extending three Paper 1 commitments into the combination operation.

C1.15 will address death. Paper 2's two death categories each inherit from Paper 1's substrate retirement commitment: functional obsolescence inherits the substrate resource release pattern; lineage supersession — retirement with archival, where archived substrate content remains substrate-addressable — inherits Paper 1's substrate-as-source-of-truth commitment as applied to retired content.

The pattern across all three lifecycle notes is the same: each lifecycle primitive (birth, mating, death) inherits from a corresponding set of Paper 1 substrate governance commitments, and Paper 2 adds entity-specific and lifecycle-specific structure beyond what Paper 1 committed to. C1.11 establishes this pattern at birth; C1.12 and C1.15 confirm it through the remainder of the lifecycle.

---

## 7. Prior-art significance

This note forecloses three classes of adversarial claim.

**Class (a): Entity-level birth governance is novel relative to Paper 1.** The claim would be that governing the origin of a named entity is a new concept, not derived from substrate content governance. This note shows that all three origination-pattern commitments travel intact from Paper 1 substrate content to Paper 2 entity birth. The governance pattern at origination is the same; what changes is the subject (named entity rather than generic substrate content) and the additional structure (level determination, DNA specification, lineage chain, birth verification). The pattern is not novel; the enrichment is.

**Class (b): The lineage anchor at birth is novel relative to Paper 1's provenance-from-origination commitment.** The claim would be that establishing an entity's position in a growing lineage chain is a new invention, unrelated to Paper 1's requirement that provenance tracking begin at origination. This note shows that the lineage anchor inherits the provenance-from-start principle directly. What is new is the chain structure — the anchor is the first link of a chain that grows through mating and selection history. The chain structure is a Paper 2 addition; the provenance-from-start principle it builds on is a Paper 1 inheritance.

**Class (c): Birth verification is novel relative to Paper 1's human-governed authorization of substrate content.** The claim would be that the birth verification step — confirming the entity satisfies its level's governance requirements before activation — is a new governance checkpoint without precedent in Paper 1. This note shows that birth verification is a structural extension of Paper 1's authorized-creation commitment. Paper 1 commits that no substrate content enters the system without governance authorization; Paper 2 adds a structured verification that the authorization has been properly instantiated at the level of the entity's structural type. The authorization requirement is inherited; the level-typed verification step is new.

---

## 8. Conclusion

Paper 2's entity birth formalization inherits Paper 1's substrate origination pattern — authorized creation, attributed record, and provenance from origination — and extends it with five new elements: entity-level naming, level determination at birth, initial DNA specification, lineage anchoring as a chain structure, and birth verification. The inheritance is not incidental; it is structural. The birth record is substrate content, and Paper 1's commitments apply to all substrate content. The governance requirement at origination is the same in both papers; what differs is the richness of what is produced by the origination event and the structural context (three-level architecture, lifecycle chain) in which that origination occurs.

Series C notes C1.12 and C1.15 complete the lifecycle inheritance triple by establishing the corresponding inheritance edges for mating variants and death. Together, C1.11, C1.12, and C1.15 establish that Paper 2's lifecycle machinery — birth, mating, death — is a systematic extension of Paper 1's substrate governance commitments into entity-level lifecycle operations, not an independent invention.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235. [Paper 1]

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235. [Paper 2]

Naja, I., Markovic, M., Edwards, P., & Cottrill, C. (2021). A knowledge graph to support the simulation and analysis of transport behaviour. *Lecture Notes in Computer Science*, 12731. (Accountability plan / accountability trace vocabulary.)

Rajabi, E., & Kafaie, S. (2022). Knowledge graphs and explainable AI in healthcare. *Information*, 13(10), 459. (Path retraceability vocabulary.)

---

## How to cite this note

Li, W. (2026). *Entity Birth Inherits Paper 1's Substrate Origination Pattern.* CKS Derivation Note #440 (Series C, C1.11). May 14, 2026. ORCID: 0009-0004-8065-3235. CC BY 4.0.
