# Paper 2 Governance Perimeter Inherits Paper 1's Governance Boundary

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 14, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work formalizes an inheritance edge between Paper 2 (Li, April 2026) and Paper 1 (Li, April 2026) of the Coordination Knowledge Substrate (CKS) theory series.

---

## Abstract

Paper 1 of the CKS series establishes a governance boundary defined by the substrate-cell architecture: human authority — the three rights of inspect, modify, and override — applies to the substrate layer; the LLM operates within cells under the governance rules that substrate content encodes; the boundary is the substrate boundary. Paper 2 extends this single boundary to a nested three-level governance perimeter covering cell scope, aspect scope, and Self scope, with human authority applying at every level and each level carrying its own governed substrate objects (DNA layer, action layer, orchestration substrates). This note formalizes the inheritance edge: Paper 2's governance perimeter strictly contains Paper 1's governance boundary (⊃), meaning that any implementation of Paper 2's nested perimeter necessarily implements Paper 1's governance boundary at cell scope. It identifies what is preserved across the inheritance — the three rights, conflict preservation, and substrate-as-source-of-truth at every level — and what is new in Paper 2: the concentric scope structure itself, the cross-level governance hierarchy, and the treatment of expression (which cell rules are activated within which aspect or Self) as a governed boundary decision. The note introduces "governance perimeter" as Paper 2's term for the extended structure, notes that full cross-paper disambiguation of this term is reserved for Series T, and provides an operational test for verifying the inheritance edge in a deployment.

---

## 1. The inheritance edge stated

The inheritance edge this note formalizes is:

> Paper 2's governance perimeter ⊃ Paper 1's governance boundary.

The ⊃ relation means strict containment: Paper 2's structure includes Paper 1's structure as a special case. An implementation that satisfies Paper 2's governance perimeter automatically satisfies Paper 1's governance boundary at cell scope; an implementation that satisfies Paper 1's governance boundary does not automatically satisfy Paper 2's governance perimeter, because Paper 2 adds three-level concentric scope structure, cross-level governance hierarchy, and expression as a governed boundary decision — none of which Paper 1 commits to.

The inheritance edge has a specific prior-art consequence. It forecloses the adversarial claim that Paper 2's governance perimeter structure is a novel invention architecturally unrelated to Paper 1's governance boundary. The nested perimeter directly extends the single boundary by applying the same principle — human authority over substrate objects — at three concentric scopes rather than one. Any party implementing Paper 2's governance perimeter necessarily traverses Paper 1's governance boundary at the innermost (cell) scope.

---

## 2. Paper 1's governance boundary: the single substrate boundary

Paper 1 establishes the governance boundary as the substrate boundary — the architectural line separating the substrate layer from the cell's execution context. Human authority applies on the substrate side of this boundary. The LLM operates on the cell side, reading from and writing to the substrate under orchestration rules, but without authority over substrate content or orchestration rules themselves.

The substrate boundary is a governance boundary, not a capability boundary. Paper 1 draws this distinction explicitly: the division between what the substrate handles and what the LLM handles is not drawn at the limit of LLM capability. It is drawn at the limit of human governance. Substrate content — the structured representations of entities, relationships, decisions, rationale, and conflicts the substrate carries — falls inside the boundary because humans must retain authority over it. LLM inference, intermediate reasoning state, and ephemeral cell context fall outside the boundary because they are execution artifacts, not authoritative coordination state.

Three rights constitute governance inside the boundary: the right to inspect any substrate content and any orchestration rule; the right to modify any substrate content and any orchestration rule; the right to override any LLM-produced output touching substrate content or orchestration rules. These three rights hold at all times as architectural properties of the system, not as procedural promises dependent on scheduling or approval workflows.

Within the governance boundary, Paper 1 commits to three additional properties that the inheritance note must track precisely, because Paper 2 preserves all three at every level of its extended structure.

First, substrate-as-source-of-truth: the substrate is the authoritative store for coordination state, not LLM memory, not external agent state, not ephemeral context. The boundary enforces this by requiring that authoritative state cross the boundary as substrate content rather than remain inside cell execution context.

Second, conflict preservation: contradictions are preserved as first-class substrate content rather than resolved silently. The governance boundary is where resolution authority is located: humans can inspect the conflict, modify the conflicting entries, or override any resolution the cell produces under orchestration rules.

Third, path retraceability: provenance metadata — writer identity, timestamp, rationale, upstream sources — attaches to substrate content as it crosses the boundary, making the derivation chain from any current substrate state back to its human-authored origins addressable.

Paper 1's governance boundary is a single boundary at a single scope: the cell. Paper 1 does not commit to what governance looks like above cell scope, because Paper 1's architectural object is the single coordination cell. This is not a gap; it is an intentional scope boundary. The extension to wider scopes is Paper 2's work.

---

## 3. Paper 2's governance perimeter: the nested three-level structure

Paper 2 extends the governance boundary to a nested three-level structure called the governance perimeter. The perimeter covers three concentric scopes: cell scope, aspect scope, and Self scope.

At cell scope, the governance objects are the cell's DNA layer (governed reasoning content defining what the cell knows and how it reasons), the cell's action layer (recorded execution state and feedback), and the cell's orchestration substrates (harness substrates governing cell-level behavior). These are the governance objects Paper 1 commits to at the substrate layer; Paper 2 gives them structural names within the DNA/action layer distinction, but their governance status is inherited directly from Paper 1.

At aspect scope, the governance objects are the aspect's DNA layer (coordination content defining the aspect's purpose and the relational roles of its constituent cells) and the aspect's action layer (execution state and feedback at aspect scope). The aspect also carries its own orchestration substrates governing how cells participate in the aspect arrangement. These are governed substrate objects that did not exist in Paper 1's single-cell scope; they are Paper 2's addition to the governance perimeter.

At Self scope, the governance objects are the Self's DNA layer (the integration architecture defining how aspects compose into one coherent whole), the Self's action layer (execution state at enterprise scope), and the Self's integration orchestration substrates governing how aspects relate to one another. These are governed substrate objects at the widest scope Paper 2 addresses.

Human authority — the same three rights, unchanged from Paper 1 — applies to all governed substrate objects at all three levels. This is the structural continuity across the inheritance edge: the principle does not change; the scope of its application widens.

The three concentric scopes form a nested perimeter: the cell governance scope sits inside the aspect governance scope, which sits inside the Self governance scope. Each level's governed substrate objects are inside the perimeter at that level. LLM execution, external tools, and adjacent systems remain outside every level of the perimeter, as they are outside Paper 1's single boundary.

Paper 2 uses "governance perimeter" to name this nested structure. The term is Paper 2's, introduced to describe a structure that Paper 1's single-boundary vocabulary does not cover — not because the principle changes, but because one term is sufficient for one scope and three concentric scopes require a term that can carry the nesting. Section 6 below treats the terminology question directly.

---

## 4. What is preserved across the inheritance

Four properties of Paper 1's governance boundary are preserved, without modification, at every level of Paper 2's governance perimeter.

**The three rights.** Inspect, modify, override apply at cell scope, aspect scope, and Self scope independently. A human with appropriate access can inspect the DNA layer of any cell, of any aspect, or of the Self; can modify any of these without requiring authorization from a higher level within the perimeter; can override any LLM-produced output touching any of these governed substrate objects. The rights are preserved in both their content (what the three rights are) and their temporal character (they are available at all times, not only at scheduled review windows).

**Conflict preservation as first-class substrate content.** Paper 1 commits to preserving contradictions as addressable substrate objects rather than resolving them silently. Paper 2 preserves this at every level: cells carry their own first-class conflicts; aspects carry conflicts arising at aspect scope from the coordination of constituent cells; the Self carries conflicts across aspects. The two-level conflict-handling structure Paper 1 establishes — substrate-level preservation, cell-level resolution under orchestration rules — extends naturally to three levels in Paper 2. The governance boundary at each level is where resolution authority is located.

**Substrate-as-source-of-truth.** The substrate is the authoritative coordination store at every scope. Cell-scope DNA and action layers are authoritative for cell coordination state. Aspect-scope DNA and action layers are authoritative for aspect coordination state. Self-scope DNA and action layers are authoritative for Self coordination state. LLM inference and ephemeral execution context are not authoritative at any level; they remain outside the governance perimeter at each scope.

**Path retraceability.** Provenance metadata attaches to governed substrate content at every level. A derivation chain from any current Self-scope DNA content back through aspect-scope and cell-scope ancestry to human-authored origins is architecturally supported by the same provenance commitment Paper 1 establishes at single-cell scope.

---

## 5. What is new in Paper 2

Three structural commitments in Paper 2's governance perimeter have no counterpart in Paper 1's governance boundary. These are not inherited; they are Paper 2's additions.

**The concentric scope structure itself.** Paper 1 commits to a governance boundary at one scope. Paper 2 commits to governance boundaries at three concentric scopes simultaneously. The nesting relationship — cell inside aspect inside Self — is a structural commitment Paper 1 had no occasion to make, because Paper 1's architectural object was the single cell. Implementing the nested perimeter requires that each of the three concentric scopes be independently governable: a human can exercise the three rights at cell scope without also exercising them at aspect scope, and vice versa. This independence-within-nesting is the structural property the concentric perimeter adds.

**The cross-level governance hierarchy.** Paper 2 commits to a hierarchy governing which changes belong at which scope. Some changes are appropriately governed at cell scope: edits to an individual cell's DNA layer, changes to a cell's orchestration substrates, overrides of cell-level LLM outputs. Some changes belong at aspect scope: changes to the relational roles through which cells participate in an aspect arrangement, edits to aspect-level DNA content, aspect-scope conflict resolution. Some changes belong at Self scope: changes to the integration architecture that defines how aspects compose, edits to Self-level DNA, overrides at Self scope. Paper 1 had no cross-level hierarchy because it had only one level. The cross-level hierarchy is a commitment about where in the governance perimeter different classes of change are authorized; it is genuinely new in Paper 2.

**Expression as a governance boundary decision.** Paper 2 commits to expression — the governed selection of which cell rules are activated within which aspect or Self scope — as a first-class governance commitment. Which of a cell's DNA content is expressed within a given aspect arrangement is a boundary decision: it determines what governed substrate content the cell contributes to the aspect's coordination work. This expression mechanism is what makes a single cell participable in multiple aspects simultaneously (relational role membership) without losing governance integrity at any scope. Paper 1's single-cell scope did not require this decision; a cell's substrate content was fully in scope without selection. The expression commitment is Paper 2's architectural addition at the governance boundary level.

---

## 6. "Governance perimeter" as Paper 2's term

Paper 1 uses "governance boundary" to name the substrate boundary. Paper 2 introduces "governance perimeter" to name the nested three-level structure. The terminological distinction reflects the structural distinction: a single boundary does not require a different word for the same concept; a nested three-level structure with concentric scopes benefits from a term that carries the nesting.

The inheritance relationship between the terms parallels the inheritance relationship between the structures: Paper 2's governance perimeter ⊃ Paper 1's governance boundary. At the innermost (cell) scope of the governance perimeter, the governance perimeter instantiates Paper 1's governance boundary. The perimeter is not a replacement for the boundary; it is the boundary extended to three concentric scopes.

One disambiguation point belongs here, though full cross-paper treatment is reserved for Series T (planned as T1.08, which will give the governance perimeter term systematic disambiguation across all three papers of the CKS series). The disambiguation point for this note is narrow: "governance perimeter" in Paper 2 is not synonymous with "governance boundary" in Paper 1, even though both name the same underlying principle. Using them interchangeably in Paper 2 contexts would lose the nesting structure. Using "governance perimeter" in Paper 1 contexts would import a structural commitment Paper 1 does not make. Series T will address the full cross-paper vocabulary; here, the note uses each term for its own paper's structure.

---

## 7. Operational test

The inheritance edge asserts that any implementation of Paper 2's governance perimeter implements Paper 1's governance boundary at cell scope. The following test verifies this claim for a given deployment.

An observer examining a deployment can ask, at each of the three governance scopes independently:

**At cell scope:** Can the observer identify the governed substrate objects at cell scope — the cell's DNA layer, action layer, and orchestration substrates? Can the observer verify that the three rights (inspect, modify, override) apply to each of these objects? Can the observer confirm that the cell's LLM execution context is outside the governance boundary and that authoritative coordination state is inside it? If yes to all three, the deployment instantiates Paper 1's governance boundary at cell scope.

**At aspect scope:** Can the observer identify the governed substrate objects at aspect scope — the aspect's DNA layer, action layer, and orchestration substrates? Can the observer verify that the three rights apply to each of these objects independently of the cell-scope governance exercise (i.e., a human can govern at aspect scope without exercising cell-scope rights, and vice versa)? Can the observer confirm that aspect-scope conflicts are preserved as first-class substrate content? If yes to all three, the deployment instantiates a governance boundary at aspect scope.

**At Self scope:** Can the observer identify the governed substrate objects at Self scope — the Self's DNA layer, action layer, and integration orchestration substrates? Can the observer verify that the three rights apply independently at this scope? Can the observer confirm that Self-scope substrate content is authoritative (the source of truth for Self-scope coordination state) and that LLM inference at Self scope does not constitute authoritative state? If yes to all three, the deployment instantiates a governance boundary at Self scope.

If all three scope tests pass, the deployment instantiates Paper 2's governance perimeter. By the inheritance edge, the first scope test (cell) is necessarily satisfied whenever any of the three pass, because the cell scope is the innermost level of the nested perimeter; the test makes this explicit by requiring all three to be checked independently, rather than inferring cell-scope satisfaction from aspect- or Self-scope satisfaction.

A deployment that passes only the cell-scope test but not the aspect or Self scope tests has implemented Paper 1's governance boundary but not Paper 2's governance perimeter. This is a coherent implementation state — it is what a Paper 1 deployment without Paper 2's extensions looks like.

A deployment that passes the aspect or Self scope tests but fails the cell-scope test is not implementing either paper's governance structure correctly: the nested perimeter requires that the innermost scope be governed, and the inheritance edge means the cell-scope governance boundary is a prerequisite, not an option.

---

## 8. Conclusion

Paper 2's governance perimeter inherits and extends Paper 1's governance boundary. The single substrate boundary Paper 1 establishes — human authority over substrate content and orchestration rules, with the three rights applying at all times — becomes the innermost level of a three-level nested governance perimeter in Paper 2. The extension is a scope extension, not a principle change: the same commitment that human authority applies to substrate objects at cell scope is applied at aspect scope and Self scope, with each level carrying its own governed substrate objects (DNA layer, action layer, orchestration substrates) and the same three rights applying at each level independently.

Three properties are preserved across the inheritance: the three rights, conflict preservation as first-class substrate content, and substrate-as-source-of-truth. Three structural commitments are new in Paper 2: the concentric scope structure itself, the cross-level governance hierarchy, and expression as a governance boundary decision.

The prior-art consequence is precise: implementing Paper 2's governance perimeter necessarily implements Paper 1's governance boundary at cell scope. No implementation of the nested perimeter can avoid traversing the innermost governance boundary Paper 1 establishes.

---

## Source papers

Li, W. (2026a). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235. [Paper 1]

Li, W. (2026b). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235. [Paper 2]
