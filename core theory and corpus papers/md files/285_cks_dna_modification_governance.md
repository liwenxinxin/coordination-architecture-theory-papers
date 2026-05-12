# DNA Modification Governance — Standard Authority Architecture Applied to DNA Layer Evolution

**Derivation Note B2.68 — Phase B2, Series B**

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 12, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in "The Instinct/Reasoning Separation Outside the Model" (Li, April 2026), the second paper in the CKS theory series following "Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems" (Li, April 2026).

## Abstract

Paper 2 specifies that directed selection — the mechanism through which CKS substrates evolve by human-governed modification of DNA layer content — is governed through the standard authority architecture from Paper 1. That standard authority architecture is the A2.01–A2.04 governance affordances: the inspect right, the modify right, the override right, and rule authoring. This note formalizes DNA modification governance as the specific application of those four affordances to DNA layer content, as defined by B2.67's scope: cell DNA (orchestration rules, behavior rules, harness rules), aspect DNA (coordination rules), and Self DNA (integration architecture and instinct/reasoning configuration). The note articulates how each affordance applies at DNA scope, how governance intensity varies across DNA content types, and how A2.47 authority distribution provides level-distinct modification authority. The note also marks the distinction between DNA modification governance and three adjacent but separate architectural matters: directed selection evolution patterns (B2.71), DNA version management (B2.69), and conventional AI directed evolution. This is the sixty-eighth Phase B2 note and the second of six notes decomposing B1.14 directed selection.

---

## 1. Why DNA modification governance needs standalone formalization

Paper 2's core theory specifies that DNA evolution — the directed selection mechanism that modifies the orchestration substrate as CKS deployment goals develop — "is governed through an authority architecture extending Paper 1 §3.3 directly." The architecture decomposes who can propose substrate changes, who can authorize them, what verification regime applies, and what reversion paths exist. B1.14 formalizes directed selection as an architectural commitment; B2.67 defines the scope of what directed selection operates over. What neither note renders explicit is how Paper 1's standard governance affordances — A2.01 through A2.04 — apply specifically to the DNA layer content that directed selection modifies.

This omission is architecturally consequential. DNA modification is not a generic substrate write operation. It modifies the orchestration rules, behavior rules, harness configurations, coordination rules, and integration architecture that govern how all other substrate operations proceed. DNA content is, in Paper 2's framing, the stabilized layer that determines cell behavior across task instances. Modifying it changes the rules under which cells operate going forward; the governance framework for that modification therefore carries a different operational weight than governance over action-layer content or transient coordination state. Formalizing DNA modification governance as a standalone derivation is what makes the application of A2.01–A2.04 to this layer explicit, testable, and resistant to downstream conflation with other governance commitments.

The note occupies the sixty-eighth position in Phase B2 and the second position in the B1.14 decomposition. B2.67 established what DNA modification governance applies to. This note establishes how governance applies to it. B2.69 (DNA version management), B2.70 (retroactivity treatment), B2.71 (directed selection evolution patterns), and B2.72 (directed selection verification) will close the B1.14 decomposition.

---

## 2. The governance precisely stated: A2.01–A2.04 at DNA scope

### A2.01 — Inspect right applied to DNA

The inspect right gives authorized humans direct read access to DNA layer content in inspectable form, at the time of their choosing, without LLM intermediation as a precondition. Applied to the DNA layer, the inspect right has a specific operational content: a human with appropriate access can read any DNA element the deployment authorizes them to see — any orchestration rule governing how a cell executes, any behavior rule defining what a cell does at a task level, any harness configuration specifying how a cell is integrated, any coordination rule governing aspect-level behavior, any integration architecture specification, and any instinct/reasoning boundary configuration — as the substrate actually carries it.

The inspect right is foundational for DNA modification governance in a specific sense: a modify or override action taken without the prior ability to read what is being changed is not governance in any architecturally robust sense. Inspection is what makes DNA content knowable to human governors, which is the precondition for directed modification. Inspection is also what makes the scope of a proposed modification evaluable before it is applied — what other rules depend on this element, what behavior will change, what cells are affected. A system in which DNA content is inspectable only after LLM-mediated reconstruction of a compiled or minified form does not satisfy the inspect right at DNA scope, even if the content is technically recoverable.

### A2.02 — Modify right applied to DNA

The modify right is the core DNA evolution operation. Under A2.02, authorized humans can modify DNA layer content: changing specific rules (rule-level modification), changing the schemas that organize DNA content (schema-level modification), changing lifecycle policies associated with DNA elements (policy-level modification), or changing harness configuration (configuration-level modification). Each of these is a distinct modification type with potentially distinct governance intensity and authority requirements, but all are instances of the A2.02 modify right applied to the DNA layer.

DNA modifications are recorded per A2.40's six provenance metadata fields — which element was changed, by whom, under what authority, at what time, with what rationale, and in what prior state — so that the modification history constitutes a retraceability record per A1.07. Retroactivity treatment applies per A6.02: historical DNA content is preserved in the substrate's version record rather than overwritten; new DNA content applies forward from the modification event. The specific mechanics of that historical preservation are the subject of B2.69 and B2.70; this note holds them as inherited commitments.

### A2.03 — Override right applied to DNA-derived decisions

The override right applies at DNA scope, but its application is architecturally distinct from the modify right in a way that matters. A2.03 override does not modify the DNA rule that produced a decision; it creates an override record that addresses a specific decision that the DNA rule produced, without changing the rule itself. A human who overrides a specific scheduling decision that a cell's orchestration rule generated is exercising A2.03; a human who changes the orchestration rule so that the scheduling decision is generated differently in all future instances is exercising A2.02.

This distinction is architecturally load-bearing for DNA modification governance. Override is lighter than modification: it requires lower authority, has no forward effect on rule operation, and does not generate a version entry in the DNA layer. Modification is heavier: it changes what the DNA layer contains, has forward effect on all cells that carry the modified element, and requires both A2.40 provenance recording and A6.02 retroactivity treatment. A governance architecture that conflates override with modification — treating them as interchangeable tools for correcting behavior — will tend to produce unauthorized DNA drift, where override records accumulate that are functionally equivalent to rule modifications but lack the governance treatment modifications require. Naming the distinction explicitly is part of what B2.68 formalizes.

### A2.04 — Rule authoring as primary mechanism

Rule authoring is the primary mechanism through which directed selection proceeds, because DNA is authored rules. Creating a new orchestration rule, modifying an existing behavior rule, deleting a harness configuration element, and adding a coordination rule at aspect scope are all rule authoring operations per A2.04. They are also all DNA modification operations per B2.67's scope. The equivalence is exact: directed selection in CKS substrates is, architecturally, the exercise of the A2.04 rule authoring affordance on DNA layer content.

The primacy of rule authoring over the other three affordances is not a ranking of importance but a description of which affordance directly constitutes the DNA evolution operation. Inspect enables it (you read what you are changing), override corrects specific decisions it produces (without changing it), and provenance records it (A2.40). But the act of DNA modification is itself rule authoring: writing or rewriting a DNA element is what directed selection does.

---

## 3. What makes DNA modification governance architecturally distinctive

Conventional AI directed evolution — fine-tuning, reinforcement learning from human feedback, supervised adaptation — also produces changes to AI behavior under human direction. What it does not provide is an explicit governance architecture that specifies, at design time, what the four affordances are, who holds each one, at which scope they apply, and what records each exercise produces. In conventional directed evolution, governance is implicit: model owners decide to initiate fine-tuning; the decision may be documented in an ML experiment log or not; the before-and-after behavior difference may be inspectable through evaluation benchmarks or not; specific decisions produced by the pre-fine-tuning model cannot be overridden independently of the model weights; rule authoring in the sense of changing specific orchestration rules is not a defined operation because rules and weights are not architecturally distinguished.

CKS DNA modification governance is architecturally explicit in four respects that conventional directed evolution is not. First, the affordances are named and defined at the pattern level, not at the deployment level — any CKS deployment inherits A2.01–A2.04 as part of the pattern's standard authority architecture, not as deployment-specific tooling decisions. Second, all four affordances are available: inspection is available before modification, not only through post-hoc evaluation; override is available for specific decisions without requiring re-training; rule authoring is an identifiable operation on identifiable DNA elements rather than an undifferentiated contribution to weight updates. Third, each exercise of the affordances produces governance records per A2.40 provenance requirements, making the modification history auditable per A1.07 retraceability. Fourth, governance authority is distributed per A2.47, so different humans hold different affordances at different levels — the architecture specifies not just that governance exists but who governs what.

---

## 4. Inherited Paper 1 commitments

DNA modification governance inherits from Paper 1 without redefense. A2.01–A2.04 are foundational: the inspect, modify, and override rights and rule authoring are Paper 1 §3.3 commitments that Paper 2 extends to DNA evolution scope without alteration. A2.40's six provenance metadata fields apply to every DNA modification event. A6.02 retroactivity treatment holds for DNA changes: historical DNA content is preserved; new DNA applies forward. A1.01 human-governed is the parent commitment: DNA modification governance is the human-governed commitment applied specifically to DNA layer content. A1.07 retraceability is what the combination of A2.40 provenance and A6.02 historical preservation produces for the DNA layer: a complete, addressable record of every modification event.

Authority distribution per A2.47 is the additional Paper 1 commitment that becomes especially salient at DNA scope. A2.47 specifies who has what authority within the CKS deployment, with that distribution itself being substrate-resident per A2.46 — the authority distribution is itself governed content. Applied to DNA modification, A2.47 provides level-distinct modification authority: different humans may hold DNA modification authority at different structural levels, with deployment architects typically holding Self-level DNA authority, operational managers typically holding aspect-level DNA authority, and cell operators typically holding cell-level DNA authority. None of these assignments are architectural requirements; they are deployment configurations within the framework A2.47 provides.

---

## 5. Governance intensity variation and authority distribution

Not all DNA modifications carry equal operational consequence, and DNA modification governance does not treat them as if they did. Governance intensity — the degree of review, authorization, and verification warranted by a given modification — varies across DNA content types based on the scope and reversibility of the modification's operational effects.

Self-level DNA changes — modifications to integration architecture, instinct/reasoning boundary configuration, and Self-level orchestration rules — warrant the highest governance intensity. A Self-level DNA change affects the entire deployment: every aspect and every cell that participates in the Self is potentially affected by a change at this level. Self-level DNA authority is typically restricted to deployment architects, and review processes for Self-level changes typically involve structured peer review before application. The high governance intensity at Self level is not an architectural requirement but a deployment configuration that the architecture makes expressible.

Aspect-level DNA changes — modifications to coordination rules that govern how cells participate in a given relational role membership — warrant moderate governance intensity. An aspect-level change affects all cells that currently participate in that aspect, but not cells whose behavior is governed by other aspects. Aspect-level DNA authority may be held by operational managers who understand the aspect's domain and can evaluate the coordination consequences of rule changes.

Cell-level DNA changes — modifications to individual cells' orchestration rules, behavior rules, or harness configurations — have variable governance intensity depending on the cell's operational stakes. High-stakes cells per B2.05 warrant review processes approaching aspect-level intensity; routine cells may proceed through lighter modification processes. Cell-level DNA authority may be held by cell operators, with the specific authority scope configured per deployment.

The variation in governance intensity across levels is what makes B1.20's recursive-levels principle architecturally productive for DNA modification governance: the same four affordances apply at every level, but the authority distribution, review requirements, and operational consequences differ by level. A flat governance architecture that treats all DNA modifications identically — regardless of level, regardless of operational stakes — has not implemented the level-distinct governance Paper 2 specifies.

---

## 6. Operational implications

DNA modification governance applies at every structural level per B1.20 recursive inheritance. Deployments configure level-distinct authority distribution per A2.47, specifying which humans hold A2.01–A2.04 at each level and under what conditions. Review processes for high-intensity changes are themselves substrate content — they are orchestration rules per A2.04 that govern how modification proposals are evaluated, who must authorize them, and what verification must occur before application. The review processes are therefore themselves modifiable under the governance framework they specify, subject to the recursive-governability commitment Paper 2 inherits from Paper 1.

Cross-partner DNA modification — modification of DNA elements that are shared or governed across multiple Selves — requires cross-partner authority per A2.47. The authority architecture for cross-partner DNA modification is more complex than for intra-Self modification: it involves multiple authority distributions from multiple deployments, with the cross-partner governance framework itself being substrate content in the shared layer. This topic extends beyond B2.68's scope and will be addressed in later Phase B2 notes.

DNA modification governance is compatible with LLM-drafted modifications. Paper 1's authority-versus-labor distinction holds throughout: humans hold authority over DNA structure, orchestration rules, and modification rights, while LLMs may draft, propose, and populate DNA content changes under that authority. LLM-drafted DNA modifications become effective only after human authorization; the authorize-then-record sequence is what preserves the A2.04 rule authoring character of the operation.

---

## 7. Limits of the commitment

DNA modification governance does not prescribe specific governance workflows. Deployments configure how modification proceeds — what approval steps exist, what review processes apply, what tools are used — within the authority framework A2.01–A2.04 and A2.47 define. The architecture specifies the affordances and their distribution; it does not specify the workflow through which the affordances are exercised.

Governance intensity variation is not an architectural requirement. The architecture does not mandate that Self-level changes require peer review or that cell-level changes may proceed through lighter processes. These are deployment configurations that the architecture makes expressible; they are not properties the pattern commits to.

A2.02 modify right is the right to modify DNA content, not a mandate that all DNA modifications must proceed under explicit authorization workflows. Deployments may configure modify authority broadly or narrowly depending on operational requirements. The right is what the architecture preserves; how and when it is exercised is deployment configuration.

DNA modification governance is not the same as directed selection evolution patterns per B2.71. Governance is the authority framework — who can modify what, under what affordances, with what records. Evolution patterns are the operational approaches through which modifications are generated, evaluated, and applied. The governance framework is what makes evolution patterns governable; it does not specify which patterns a deployment uses.

DNA modification governance is not the same as DNA version management per B2.69. Governance is the affordance framework — the rights architecture for modification. Version management is the history mechanism — how modification events are recorded as addressable version states. B2.69 formalizes the specific version management commitment; B2.68 establishes the governance framework within which version management operates.

---

## 8. One-sentence test

A CKS deployment implements DNA modification governance if and only if authorized humans can inspect any DNA element directly, can modify any DNA element with the modification recorded per A2.40 and treated per A6.02, can override specific decisions that DNA rules produced without modifying the rules, can author new DNA elements as the primary directed selection operation, with each of these affordances distributed per A2.47 at level-distinct scope across cell, aspect, and Self levels.

---

## 9. Why naming this as standalone matters

DNA modification governance is the application of Paper 1's standard authority architecture to Paper 2's directed selection mechanism. Naming it as a standalone derivation does three things. First, it makes the specific application of A2.01–A2.04 to DNA layer content explicit and testable independently of the broader directed selection commitment. Second, it places the override/modify distinction — architecturally critical for preventing unauthorized DNA drift — in the public record as a formalized design specification. Third, it establishes the governance intensity variation and level-distinct authority distribution framework as prior art, narrowing the territory where any party could claim novel invention of explicit governance frameworks for AI orchestration rule modification.

This note is the sixty-eighth in Phase B2 and the second of six decomposing B1.14. B2.67 (directed selection scope) defined what DNA modification governance applies to. B2.68 (this note) formalizes how the governance applies. B2.69 (DNA version management), B2.70 (retroactivity treatment), B2.71 (directed selection evolution patterns), and B2.72 (directed selection verification) will complete the B1.14 decomposition. Subsequent Phase B2 notes will continue with B1.15 multi-shaped governance decomposition.

---

## Cross-references

**Directly load-bearing:** B1.14 (directed selection); B2.67 (directed selection scope); A2.01 (inspect right); A2.02 (modify right); A2.03 (override right); A2.04 (rule authoring); A2.47 (authority distribution); A2.40 (six provenance metadata fields); A6.02 (retroactivity); A1.07 (retraceability); A1.01 (human-governed); B1.20 (CKS exceeds biology: recursive levels)

**Directly relevant:** B2.28 (layer-level governance affordances); B2.05 (high-stakes cells); A2.46 (authority distribution as substrate content)

**Downstream:** B2.69 (DNA version management); B2.70 (retroactivity treatment for DNA changes); B2.71 (directed selection evolution patterns); B2.72 (directed selection verification)
