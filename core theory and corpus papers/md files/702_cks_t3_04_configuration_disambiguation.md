# Disambiguating "Configuration" Across the Trilogy

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 15, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes commitments across the CKS theory trilogy: *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026), and *Inter-Self Coordination via Shared Substrate / Full Aspect Integration* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to articulate, in operational form, the precise meaning of the term *configuration* as that term is used across the three source papers, so that downstream work can adopt or argue against the term without ambiguity.

## Abstract

The term "configuration" appears throughout the CKS trilogy at two distinct levels of abstraction. At the general level, running through all three papers, "configuration" names the architectural principle that governance specifications governing any aspect of the system are authored as substrate content — inspectable, modifiable, and subject to the same authority architecture as all other substrate content. At the specific level, introduced in Paper 3, "FAI configuration" names a particular named governance artifact: the authored document specifying the six dimensions that fully constitute a Full Aspect Integration (FAI) event. The general principle is established in Paper 1 and extended through Papers 2 and 3; the specific FAI configuration artifact is a Paper 3 application of that principle at inter-Self scope. Paper 2 contributes a third usage that bridges the two: the DNA layer of each cell, aspect, and Self is that entity's configuration — understanding this is what makes directed selection (DNA absorption) legible as a configuration change rather than as mere data entry. This note states all three usages precisely, identifies the disambiguation, and provides an operational test for distinguishing which usage is operative in a given context.

## 1. Why disambiguation is needed

The word "configuration" does significant load-bearing work in all three CKS papers, and the work differs across papers. In Paper 1, the orchestration rules that govern a cell's behavior are authored as substrate content — this is configuration in the sense of governance-as-authored-content. In Paper 2, the DNA layer of every cell, every aspect, and every Self constitutes that entity's governance specification — the DNA layer *is* the entity's configuration. In Paper 3, the term "FAI configuration" names a specific governance document that a practitioner constructs when standing up a FAI event.

Without disambiguation, three failure modes arise. A reader of Paper 3 who encounters "FAI configuration" may mistakenly treat it as equivalent to the general Paper 1 principle, collapsing the specific artifact into the background architecture. A practitioner implementing Paper 2's directed selection (DNA absorption from a foreign Self) may not recognize the operation as a configuration change, underestimating its governance implications. And a reader scanning all three papers may perceive "configuration" as drifting across them — an apparent inconsistency that is not inconsistency but scope-specific application of one underlying commitment.

This note closes all three failure modes.

## 2. The general principle: configuration as substrate content (Papers 1, 2, 3)

The general principle is stated most directly in Paper 1: governance specifications governing cell-level behavior are authored as substrate content, not embedded in the LLM, not encoded in runtime middleware, and not implicit in deployment conventions. Orchestration rules, conflict-handling rules, compliance requirements, and escalation policies are substrate content. They are subject to the same three governance rights — inspect, modify, override — that apply to all substrate content. This is not a trivial commitment: it means governance lives where everything authoritative lives, in the substrate, and is governed the same way.

Paper 2 extends this principle to the three-tier structure without modifying it. At cell scope, the DNA layer carries orchestration rules as substrate content — cell configuration. At aspect scope, the DNA layer specifies which governance territory the aspect covers and how cells within it coordinate — aspect configuration. At Self scope, the DNA layer integrates governance specifications across all aspects — Self configuration. The principle is the same at every tier; the scope of the governance specification varies.

Paper 3 further extends the principle to inter-Self scope. The shared substrate that mediates a FAI event is itself governed: its structure, its governance perimeter, and the dimensions of the coordination it enables are all substrate content authored under joint human authority across participating Selves' governance. Paper 3 §8 makes this explicit: every dimension of the FAI mechanism is itself substrate content, and configuration of configuration substrate is also substrate content. The recursion bottoms out at human-authored governance authority per Paper 1 §3.3.

The general principle, precisely stated: *governance specifications governing the operation of any component of the governed system — at any scope, at any tier, within any FAI event — are authored as substrate content subject to the three governance rights.*

## 3. The DNA layer as configuration (Paper 2)

Paper 2's most consequential application of the general principle is the identification of the DNA layer as the configuration layer within every cell, aspect, and Self. The DNA layer carries stabilized orchestration content — governance rules, conflict-handling rules, lifecycle policies, schemas — that defines what the entity is governed to do. The action layer records what the entity has done. The DNA layer is authored governance content; it is the entity's configuration in the most direct sense.

This identification has an important downstream implication for evolution: directed selection (one of Paper 2's three evolution mechanisms) is the process by which a Self absorbs DNA-layer content from a foreign Self, typically through a FAI event, and integrates it into its own DNA layer. Because the DNA layer is the Self's configuration, directed selection is fundamentally a configuration change — it modifies what the Self is governed to do, not merely what it has recorded as experience. A practitioner who does not recognize directed selection as a configuration change may treat it as a data-entry operation and fail to apply the governance authority architecture that configuration changes require: human authority over what governance specifications take effect in the substrate.

The disambiguation at Paper 2 scope: *the DNA layer IS the entity's configuration; modifying it — whether by direct authoring or by directed selection — is a configuration change and requires the governance authority architecture that any configuration change requires.*

## 4. The FAI configuration artifact (Paper 3)

Paper 3 introduces a specific named governance artifact, distinct from the general principle: the FAI configuration. The FAI configuration is a document, authored as substrate content before a FAI event is initiated, that specifies the six dimensions constituting the event. It is not a background architectural property; it is a produced artifact that a human (or an LLM operating under human direction) authors, deposits into the shared substrate, and governs.

The six dimensions that the FAI configuration must specify are:

1. **Sharing scope** — which aspects, from each participating Self, are contributed to the shared substrate for the duration of the FAI event.
2. **Cardinality** — how many Selves participate in the event.
3. **Persistence policy** — which content, if any, persists in the shared substrate after the FAI event dissolves; all other content is ephemeral.
4. **Cooperation/competition variant** — whether the event's operating posture is cooperative (aspects working toward a shared goal), competitive (aspects tested against each other), or a specified hybrid.
5. **Provenance carry-over depth** — how many levels of provenance chain each piece of contributed content carries with it into the shared substrate.
6. **Provenance preservation on internalization** — whether provenance chains are preserved when content absorbed from the shared substrate is internalized into a participating Self's DNA layer during directed selection.

These six dimensions are not categories from which a practitioner selects; they are the complete specification that must be authored for a FAI event to be constituted under governance. An event initiated without an authored FAI configuration is an event without a governance specification — it operates outside the substrate-content commitment. The FAI configuration is what makes the FAI event human-governable.

The disambiguation at Paper 3 scope: *"FAI configuration" refers to the specific six-dimension governance document; it is one instance of the general principle of configuration-as-substrate-content, applied at the scope of a particular FAI event.*

## 5. The disambiguation table

| Term | Scope | What it is | Which papers |
|---|---|---|---|
| Configuration (general principle) | Any scope, any tier | The architectural commitment that governance specifications are authored as substrate content, inspectable and modifiable under human authority | P1, P2, P3 |
| DNA layer as configuration | Cell, aspect, Self | The DNA layer of any entity is that entity's authored governance specification; modifying it is a configuration change | P2, P3 (by inheritance) |
| FAI configuration (specific artifact) | A single FAI event | The authored six-dimension governance document that constitutes a specific FAI event | P3 specifically |

The key relationship: the FAI configuration artifact is one instance of the general principle. The general principle establishes that governance specifications must be authored as substrate content; the FAI configuration is the governance specification for one FAI event, authored as substrate content under joint authority. Neither subsumes the other; they operate at different levels of abstraction.

## 6. Operational test

A practitioner reading or implementing CKS-trilogy architecture can apply the following test to determine which usage is operative:

1. **Is the passage discussing the architecture's governing commitment that all governance specifications live in the substrate?** → General principle (Papers 1/2/3). The term names the background architectural property, not a produced artifact.

2. **Is the passage discussing the DNA layer of a cell, aspect, or Self, or a directed-selection operation that modifies it?** → DNA-layer-as-configuration usage (Paper 2). The DNA layer is the entity's authored governance specification; directed selection is a configuration change requiring human authority over what takes effect.

3. **Is the passage discussing the construction or governance of a specific FAI event — what aspects participate, how many Selves, what persists, what variant applies?** → FAI configuration artifact (Paper 3). A specific six-dimension governance document is being constructed, authored, or governed. Verify that all six dimensions are specified; an incomplete FAI configuration is a governance gap.

A system in which FAI events are initiated without an authored FAI configuration treats the event as infrastructure rather than as governed coordination — a violation of the general principle the specific artifact instantiates.

## 7. Conclusion

"Configuration" in the CKS trilogy names one architectural commitment at three levels of specificity. The general principle — governance specifications authored as substrate content — runs through all three papers without modification, only scope expansion. The DNA layer as configuration names Paper 2's specific application of the principle at the entity level and reveals why directed selection is a configuration change with governance implications. The FAI configuration artifact names Paper 3's specific application of the principle at the FAI event level, requiring an authored six-dimension governance document before any FAI event is constituted.

Downstream work that adopts the CKS pattern should use "FAI configuration" only for the specific six-dimension artifact, and "configuration" (unqualified) for the general principle. Treating the FAI configuration artifact as the general principle conflates a specific governance document with the background architectural commitment it instantiates. Treating DNA absorption as data entry rather than as configuration change misses the governance authority implications Paper 2 establishes. Both misreadings are foreclosed by the disambiguation this note formalizes.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Inter-Self Coordination via Shared Substrate / Full Aspect Integration.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Disambiguating "Configuration" Across the Trilogy.* May 15, 2026. ORCID: 0009-0004-8065-3235.
