# Recursive Conflict-as-First-Class (A1.03): How the Conflict Preservation Commitment Applies at Cell, Aspect, and Self Scope

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026). It is the eleventh of thirteen derivation notes decomposing B1.20 (recursive Paper 1 commitments) and does not introduce new axioms. Its contribution is to formalize, in operational terms, how the conflict-as-first-class commitment (A1.03) applies recursively at cell, aspect, and Self granularity within the three-level architecture Paper 2 establishes.

## Abstract

Paper 1's conflict-as-first-class commitment (A1.03) specifies that contradictions in substrate content are preserved as first-class addressable state, never silently resolved by any LLM operation or automated process, with resolution logic authored by humans and recorded as substrate content. Paper 2 extends the CKS architecture to three levels — cell, aspect, and Self — and inherits all Paper 1 commitments at every level. This note formalizes recursive A1.03: the commitment that conflicts are registered and preserved as first-class governance signals at each of the three levels, with level-specific conflict types and level-specific conflict registries. Cell-level conflicts are within-cell rule contradictions recorded in the cell's conflict registry. Aspect-level conflicts are within-aspect coordination contradictions recorded in the aspect's conflict registry. Self-level conflicts are cross-aspect integration contradictions recorded in the Self's conflict registry. The three registries together form a deployment-wide conflict visibility hierarchy. What is constant across all levels is the preservation principle: conflicts are never silently resolved. What differs across levels is what constitutes a conflict at each scope. Conflict levels are operationally independent; root cause analysis across levels is a governance activity, not an architectural requirement.

---

## 1. Why recursive conflict-as-first-class needs to be formalized as a standalone operational variant

Paper 1's A1.03 commitment operates at cell scope: substrate-level preservation of contradictions as live, addressable state, and cell-level resolution under human-authored orchestration rules. The commitment is two-leveled — preservation and resolution are coupled halves of a single architectural property — but it is scoped to the substrate-cell boundary as Paper 1 defines it.

Paper 2 extends that architecture. Three levels now structure the CKS-governed entity: cell, aspect, and Self. Multiple cells compose into aspects; multiple aspects compose into Selves. At each additional level, new kinds of coordination conflicts become possible. Cells within an aspect may produce conflicting outputs for the same coordination purpose. Coordination rules within an aspect may contradict one another. Aspects within a Self may compete for the same operational territory or produce integration contradictions. None of these conflict types exists at Paper 1's single-cell scope; all of them require A1.03's preservation principle to apply if the governance properties that make CKS coherent are to hold across the extended architecture.

Paper 2 specifies through B1.20 that all Paper 1 commitments apply recursively at every level. B2.108 formalizes what that specification means for A1.03 in particular: entity-level conflict registries at cell, aspect, and Self granularity; level-specific conflict types; and a conflict registry hierarchy that provides complete deployment-wide conflict visibility. This formalization is the eleventh in the B1.20 per-commitment decomposition series, following B2.98 through B2.107, and is the last per-commitment formalization before B2.109 (recursive operational tests) and B2.110 (recursive commitments verification), which will close the B1.20 decomposition and complete Phase B2.

The strategic prior-art posture of this note is the same as the series: to establish public record of the recursive conflict registration architecture, with entity-level conflict registries and a deployment-wide conflict visibility hierarchy, as derivations from the source papers under the author's name.

---

## 2. The recursive application stated precisely

### 2.1 A1.03 at cell scope: within-cell rule conflicts registered as first-class

At cell scope, A1.03 applies as Paper 1 specifies it, extended to three conflict types that arise within a cell in the multi-level architecture.

**Cell DNA rule conflicts.** When two behavior substrates within the same cell — the stabilized orchestration and behavior content that constitutes the cell's DNA layer — specify conflicting behavior for the same input type, the conflict is registered as first-class. The conflicting rules are preserved in their original form; neither is silently deleted or overwritten. Governance review addresses the conflict through directed selection per B1.14 at cell scope.

**Cell content-domain conflicts.** When a cell's input domain specification contains internal contradictions — an inclusion rule and an exclusion rule applying to the same content class, or boundary rules that produce logically inconsistent scope — the conflict is registered. Content-domain boundary rules are substrate content; their contradictions are substrate-level conflicts.

**Cell operational conflicts.** When the cell's instinct-layer output (the LLM's inference product) conflicts with the cell's DNA rules — producing content the rules do not authorize, or failing to produce content the rules require — the conflict is registered per the verification gate mechanism (B2.06). The LLM's output and the rule it violates are both preserved as substrate content.

**Cell conflict registry.** Cell-level conflicts are recorded in the cell's own conflict registry. The registry is substrate-resident per A1.08: it is addressable, persistent, and subject to the three human governance rights (inspect, modify, override) at all times. Conflict entries carry the standard provenance metadata — writer, timestamp, rule reference, and rationale where supplied.

**Cell conflict resolution.** Governance addresses cell-level conflicts through directed selection per B1.14 at cell scope: modifying the cell's DNA rules, deprecating the conflicting rule, or adding a superseding rule. The conflicting rules persist in the registry after resolution; resolution is recorded as new substrate content layered over the conflict, not as deletion of it.

### 2.2 A1.03 at aspect scope: coordination conflicts registered as first-class

At aspect scope, A1.03 applies to conflicts arising within a coordination arrangement of cells. Aspects operate over their constituent cells as content domain; aspect-level coordination conflicts are conflicts among the cells' outputs or among the coordination rules that govern the aspect's behavior.

**Cell output conflicts.** When member cells produce conflicting outputs for the same coordination purpose — two cells produce contradictory content that the aspect must integrate or arbitrate — the aspect registers the conflict. The conflicting outputs are preserved as aspect-level conflict entries; neither output is silently discarded. Aspect conflict-handling rules per B2.16 specify what behavior the aspect executes in the presence of the registered conflict.

**Coordination rule conflicts.** When two aspect coordination rules contradict one another — invocation rules that produce incompatible cell-triggering behavior, or output-integration rules that specify incompatible merge behavior for the same content type — the conflict is registered. The contradicting rules are preserved; the conflict entry identifies both rules and their point of contradiction.

**Membership conflicts.** When aspect membership rules per B2.16 produce contradictions about which cells are members of the aspect — inclusion and exclusion rules applying to the same cell, or rules that produce unsatisfiable membership conditions — the conflict is registered.

**Aspect conflict registry.** Aspect-level conflicts are recorded in the aspect's conflict registry, distinct from any member cell's conflict registry. The aspect registry is substrate-resident and carries full provenance metadata. Governance inspects and modifies the aspect registry through the same three rights that govern all substrate content.

**Aspect conflict resolution.** Governance addresses aspect-level conflicts through aspect DNA modification per B2.16 directed selection: revising coordination rules, clarifying membership rules, or modifying output-integration rules to eliminate the contradiction. Resolution is recorded as new substrate content; the conflicting entries persist.

### 2.3 A1.03 at Self scope: cross-aspect integration conflicts registered as first-class

At Self scope, A1.03 applies to conflicts arising in the integration of multiple aspects within one Self. The Self is the integrated whole holding coexisting aspects; cross-aspect conflicts are conflicts among the aspects' outputs or among the integration rules that govern how aspects coexist.

**Cross-aspect conflicts.** When aspects integrated within the same Self produce conflicting outputs for the same operational territory — two aspects each producing authoritative content over the same domain — or when aspects compete for the same operational resources in incompatible ways, the Self registers the conflict. The Self integration architecture per B2.21 includes cross-aspect conflict handling. The conflicting aspect outputs are preserved as Self-level conflict entries; neither output is silently suppressed.

**Integration rule conflicts.** When Self integration architecture rules contradict one another — cross-level access rules that produce incompatible read/write authorization for the same cell, or aspect coexistence rules that produce unsatisfiable structural arrangements — the conflict is registered. Both conflicting rules are preserved in the Self's conflict registry with provenance metadata.

**Self conflict registry.** Self-level conflicts are recorded in the Self's conflict registry, distinct from both cell and aspect conflict registries. The Self registry is substrate-resident, addressable, and subject to full human governance rights. The registry holds the cross-aspect conflict entries that neither the cell nor aspect registries would capture, since those registries are scoped to within-cell and within-aspect conflicts respectively.

**Self conflict resolution.** Governance addresses Self-level conflicts through Self DNA modification: revising integration rules, clarifying aspect coexistence rules, or modifying cross-level access rules. Resolution is recorded as new substrate content; conflicting entries persist.

### 2.4 What is constant and what differs across levels

**Constant — the conflict preservation principle.** At every level, the invariant is the same: conflicts are not silently resolved. Conflicting content is preserved as first-class addressable substrate state in the level's conflict registry. No LLM operation, automated coordination process, or runtime middleware layer may collapse a registered conflict without either direct human action or a human-authored orchestration rule explicitly authorizing the collapse for the specific case. This invariant is what makes A1.03 a recursive commitment rather than a level-specific one.

**Differs — what constitutes a conflict at each level.** Cell-level conflicts are within-cell rule contradictions: DNA rule conflicts, content-domain contradictions, and instinct-layer operational conflicts against DNA rules. Aspect-level conflicts are within-aspect coordination contradictions: cell output conflicts, coordination rule conflicts, and membership conflicts. Self-level conflicts are cross-aspect integration contradictions: competing aspect outputs and integration rule conflicts. These conflict types are architecturally distinct; a cross-aspect conflict registered in the Self's registry is not the same artifact as a cell DNA rule conflict registered in a member cell's registry, even if the two are causally related.

**The conflict registry hierarchy.** Cell conflict registries, aspect conflict registries, and Self conflict registries together form a deployment-wide conflict visibility architecture. A governance review of a deployment can inspect all three levels of registry to build a complete picture of where operational tensions exist. Unresolved conflicts remaining in any registry at any level signal that governance attention is needed at that scope.

---

## 3. What makes recursive conflict-as-first-class architecturally distinctive

The architectural alternative against which recursive A1.03 defines itself is implicit priority resolution: when two rules conflict, one wins by position, weight, or specificity, and the losing rule is effectively suppressed. This pattern is common in AI architectures that handle multi-rule or multi-component coordination — priority queues, rule-ranking systems, default-override hierarchies. In those architectures, the conflict is resolved at the point of encounter; what remains in the system is only the winning behavior. The governance implication of that pattern is that the losing behavior, and the tension that produced the conflict, are invisible to anyone inspecting the system after the fact.

Recursive A1.03 inverts this. At every level of the three-level architecture, conflicts are the content that is preserved, not the resolution. Resolutions are recorded on top of conflicts as new substrate content, not in place of them. This means governance can always see what the system's operational tensions were at each level, not only what the currently active behavior is. Entity-level conflict visibility — seeing conflicts at cell granularity, at aspect granularity, and at Self granularity — enables governance to identify where in the architecture a tension originates, not merely that a tension was resolved at some point.

The conflict registry hierarchy is the architectural artifact that makes deployment-wide conflict visibility possible. A deployment without level-specific registries cannot distinguish between a conflict that exists only within one cell's DNA and a conflict that crosses aspect boundaries and affects integration behavior. Level-specific registries make that distinction explicit and inspectable.

---

## 4. Biological analog as conceptual scaffold

The biological analog that motivated Paper 2's architecture extends naturally to conflict registration. Biological immune systems detect conflicting signals at multiple levels: within cells (conflicting molecular signals triggering incompatible responses), within tissues (conflicting cellular states that immune responses register), and at organism level (systemic conflicts between immune compartments). Detection at each level produces a registered response that the immune system can address at the appropriate scope. The organism does not require that a cell-level conflict automatically propagate as an organism-level response; the conflict is registered at the scope where it occurs, and cross-level responses emerge from governance logic, not from automatic propagation.

Recursive A1.03 is the governed architectural analog. Conflicts are registered at the level where they occur: within cells, within aspects, within Selves. Cross-level responses — governance activity addressing a Self-level conflict that turns out to have a root cause at cell scope — are the result of human inspection and directed selection, not automatic escalation. The analogy ends where all biological analogy in Paper 2 ends: CKS registries are explicit, addressable, human-inspectable substrate content with full provenance metadata, while biological conflict detection operates through molecular and biochemical mechanisms that have no direct architectural analog in governance design.

---

## 5. Inherited Paper 1 commitments

Recursive A1.03 is not introduced by Paper 2; it is A1.03 applied to the three-level structure Paper 2 establishes. The following Paper 1 and Paper 2 commitments are directly load-bearing.

**A1.03 (conflict-as-first-class)** is the commitment being formalized recursively. The preservation principle and the coupling between preservation and resolution are inherited without modification. What Paper 2 adds is not a different commitment but the specification that the same commitment applies at every level.

**A2.40 (provenance metadata)** applies to conflict registry entries at every level. Conflict registrations are substrate content and carry the six-field provenance metadata — writer, timestamp, rule reference, rationale, addressability identifier, and conflict-party references — that A2.40 specifies for all substrate content. Without provenance, a conflict registry entry is not addressable substrate state; it is a log, and logging is not the same as first-class preservation.

**B2.16 (aspect coordination conflict-handling rules)** specifies the aspect-level mechanism: coordination rules that govern how aspects respond to registered cell output conflicts, how membership conflicts are handled, and how output-integration proceeds in the presence of preserved coordination conflicts. B2.16 is the aspect-scope analog of A1.03's cell-level orchestration rule mechanism.

**B2.21 (Self integration architecture)** specifies the Self-level mechanism: integration rules that govern how the Self responds to registered cross-aspect conflicts, how integration rule conflicts are addressed, and how aspect coexistence behavior is specified in the presence of preserved integration conflicts. B2.21 is the Self-scope analog of A1.03's cell-level resolution mechanism.

**B1.14 (directed selection — horizontal and vertical evolution)** is the resolution mechanism at every level. Governance addresses registered conflicts through directed selection: choosing which rule to revise, which DNA to modify, or which integration architecture to update. Directed selection is the process by which governance converts a conflict registry entry into a resolved state; the conflict entry persists after resolution as a record of what was addressed and when.

---

## 6. Operational implications

**Monitor conflict registries at each level.** Deployments that implement the three-level architecture maintain three classes of conflict registry: cell registries (one per cell), aspect registries (one per aspect), and Self registries (one per Self). Governance inspection of the deployment includes inspecting all three classes. A deployment in which only one level of registry is monitored has incomplete conflict visibility; conflicts at unmonitored levels accumulate without governance attention.

**Conflict patterns inform directed selection.** A cell conflict registry that shows frequent recurrence of the same DNA rule conflict type is a signal that the cell's DNA requires refinement — the rules are not well-specified enough to avoid repeated contradictions. An aspect conflict registry with persistent cell output conflicts may indicate that the aspect's coordination rules are not adequately directing cell invocation. These patterns are inputs to directed selection decisions; governance uses conflict registry contents to identify where rule refinement is most needed.

**Cross-level conflict correlation as governance activity.** Conflict levels are architecturally independent: a conflict registered in a cell's registry does not automatically generate a conflict entry in the containing aspect's registry. However, a governance review that observes conflict entries at multiple levels in related artifacts may identify causal connections — a DNA rule conflict at cell scope that causes the cell to produce inconsistent outputs, which in turn produces a coordination conflict at aspect scope. Correlating across levels is a governance activity that requires inspection of multiple registries, not an architectural requirement that produces automatic cross-level propagation.

**Root cause analysis.** Identifying the root cause of a conflict — determining whether a Self-level integration conflict is a symptom of a cell-level rule problem or a genuinely aspect-level coordination design issue — is governance work. The architecture provides the visibility (through level-specific registries) and the modification rights (through directed selection) that root cause analysis requires. It does not specify root cause analysis procedures; those are governance-level design choices.

---

## 7. Limits

**Recursive A1.03 does not guarantee all conflicts are detected.** The commitment is that detected conflicts are registered. Whether a conflict is detected in the first place depends on the governance rules that specify detection conditions — the verification gate mechanisms at cell scope, the coordination rule conflict-detection logic at aspect scope, and the integration rule conflict-detection logic at Self scope. Gaps in detection logic produce gaps in conflict registration; those gaps are governance problems, not violations of A1.03.

**Conflict registration is not conflict resolution.** The conflict registry hierarchy provides visibility; it does not provide resolution. A deployment with full conflict visibility and no governance attention to the registered conflicts has not resolved those conflicts; it has documented them. Resolution requires governance action — directed selection at the appropriate level — and produces new substrate content recording what was decided and under what rule.

**Conflict registries are governance signals, not governance decisions.** An entry in a cell's conflict registry signals that governance attention is needed at cell scope. It does not specify what the resolution should be, which rule should be favored, or how quickly the conflict must be addressed. Governance decisions are made by humans exercising authority over substrate content, not by the conflict registration mechanism itself.

**Conflict levels are operationally independent.** A cell-level conflict does not automatically produce an aspect-level conflict entry. An aspect-level conflict does not automatically produce a Self-level conflict entry. Each level's registry contains only the conflicts that were detected and registered at that scope. Cross-level causal analysis is governance work.

**Root causes may cross levels.** A conflict registered at Self scope may have its root cause at cell scope. The architecture provides the inspection rights that allow governance to trace this connection; it does not perform the tracing automatically. Root cause analysis is a governance activity, and its outcome — a rule revision at the appropriate level — is recorded as new substrate content at that level's registry.

---

## 8. Operational test

A deployment instantiates recursive conflict-as-first-class (A1.03) if and only if all of the following hold:

Given any conflict detected at cell scope (DNA rule conflict, content-domain contradiction, or operational conflict), the conflict is recorded in the cell's conflict registry as addressable substrate content with full provenance metadata; neither conflicting element is silently discarded or modified; governance can inspect, modify, and override the registry entry at any time; and resolution is recorded as new substrate content without deleting the original conflict entry.

Given any conflict detected at aspect scope (cell output conflict, coordination rule conflict, or membership conflict), the conflict is recorded in the aspect's conflict registry with full provenance metadata; neither conflicting output or rule is silently discarded; and the same governance and resolution properties hold.

Given any conflict detected at Self scope (cross-aspect conflict or integration rule conflict), the conflict is recorded in the Self's conflict registry with full provenance metadata; neither conflicting aspect output or rule is silently suppressed; and the same governance and resolution properties hold.

A deployment that silently resolves any detected conflict at any level — whether by implicit priority, rule-ranking, or automated suppression outside a human-authored orchestration rule explicitly authorizing the collapse — does not instantiate recursive A1.03, regardless of how it handles conflicts at other levels.

---

## 9. Why naming recursive A1.03 as a standalone derivation matters

A1.03 in Paper 1 is a two-level commitment: substrate-level preservation and cell-level resolution under orchestration rules. The commitment is architecturally significant at Paper 1's single-cell scope. When Paper 2 extends the architecture to three levels, the question of how A1.03 applies is not automatically answered by Paper 1's specification. Does A1.03 apply only at cell scope within the three-level structure? Does it apply at every level independently? If it applies at every level, what counts as a conflict at each level, and what is the resolution mechanism at each?

B2.108 answers these questions by formalizing the recursive application. The formalization establishes that three distinct conflict types exist across the three levels; that three distinct conflict registries hold these conflicts; that the registries together form a deployment-wide conflict visibility hierarchy; and that the preservation principle is invariant across all three levels while the conflict type and resolution mechanism are level-specific. Without this formalization, each of these points is implicit in Paper 2's inheritance language but not stated precisely enough to function as standalone prior art.

As the eleventh per-commitment formalization in the B1.20 decomposition, B2.108 completes the series for the conflict-handling dimension of the CKS architecture across all three levels of Paper 2's structure. The next two notes — B2.109 (recursive operational tests) and B2.110 (recursive commitments verification) — will close the B1.20 decomposition and complete Phase B2 of the derivation series.

---

## Source papers

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Recursive Conflict-as-First-Class (A1.03): How the Conflict Preservation Commitment Applies at Cell, Aspect, and Self Scope.* May 12, 2026. ORCID: 0009-0004-8065-3235.
