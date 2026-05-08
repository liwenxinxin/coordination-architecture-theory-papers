# Cross-Level Access Where Purpose Requires: Non-Strict Hierarchy as a Foundational Architectural Commitment in the Coordination Knowledge Substrate Pattern's Self-Level Structure

**Author:** Wenxin Li (Independent Researcher)
**ORCID:** 0009-0004-8065-3235
**Date:** May 7, 2026
**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## Attribution

This work derives from and formalizes the instinct/reasoning separation pattern introduced in *The Instinct/Reasoning Separation Outside the Model* (Li, April 2026), the second paper in the CKS theory series following *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems* (Li, April 2026). It does not introduce new axioms. Its sole contribution is to formalize one foundational architectural commitment of Paper 2's three-level structure — that **access patterns are not strictly hierarchical**, with cross-level access enabled where purpose requires — as a standalone architectural commitment with independent operational content, distinct from the level-distinction commitment that establishes cell, aspect, and Self as architecturally distinct levels, and complementary to the content-domain relationship that describes how higher levels typically operate over lower levels.

## Abstract

Paper 2 introduces three architectural levels — cell, aspect, and Self — and specifies that higher levels operate over lower levels as content domain through pattern questions. A separate derivation note formalizes that content-domain relationship as the typical inter-level pattern. But the source paper also explicitly commits to a property that pulls in the opposite direction: access patterns are not strictly hierarchical, and the Self can access cells directly when purpose requires. This is a load-bearing operational commitment, distinct from the level-distinction commitment and from the content-domain commitment. This note formalizes it as a standalone foundational commitment. The commitment is named as the non-strict-hierarchy property: while the standard pattern is content-domain (aspects access cells; Selves access aspects), cross-level access (the Self accessing cells directly, bypassing aspect-level coordination) is operationally available where purpose requires, configured per deployment through human-authored orchestration rules, recorded with provenance, and subject to all Paper 1 governance commitments. The commitment is what distinguishes Paper 2's structural framework from rigid hierarchical AI orchestration — where bypassing intermediate layers would violate the architecture — and from biology, where access patterns through tissues, organs, and systems are largely strict by physical necessity. This note states the commitment, distinguishes it from the level-distinction and content-domain commitments it composes with, identifies the inherited Paper 1 commitments that govern its exercise, enumerates the operational scenarios it makes available, names the limits, and provides an operational test for whether a given system instantiates it.

## 1. Why cross-level access needs to be formalized as a standalone foundational commitment

Paper 2's three-level structure — cell, aspect, Self — is the architectural scaffold on which the rest of Paper 2 builds. The level-distinction commitment is formalized in B1.02 as architectural axiom: cells are atomic CKS units, aspects are coordination arrangements of cells serving particular purposes, Selves are integrated wholes holding multiple aspects. The relational-role commitment is formalized in B1.17: structural roles are not intrinsic; the same underlying CKS artifact can participate as a cell in one arrangement, as part of an aspect in another, or simultaneously across multiple aspects. The content-domain commitment is formalized in B1.18: higher levels relate to lower levels as content domain rather than as command — aspects ask pattern questions across their constituent cells, the Self holds aspects as facets of one whole.

Together those three commitments would still leave one operational question undefended. If aspects are the coordination arrangements through which the Self engages with cells, must every Self-to-cell interaction route through some aspect? The source paper explicitly answers no. In the *Level relationships* subsection of *Three levels of structure*, Paper 2 commits that "access patterns are not strictly hierarchical. The Self can access cells directly when purpose requires." A few sentences later, the paper names "cross-level access patterns enabled where purpose requires" as one of the structural arrangements that are themselves evolvable.

This is not a casual remark. It is a commitment to operational flexibility that distinguishes Paper 2's structural framework from rigid hierarchical AI orchestration, where the entire architectural point of an intermediate layer is that it cannot be bypassed. It is also a commitment that pulls in tension with the content-domain commitment in B1.18. Without standalone treatment, the tension would be left implicit, and downstream readers would either over-read the content-domain framing as strict hierarchy (collapsing CKS into a layered orchestrator) or under-read the level-distinction commitment (treating cross-level access as evidence the levels are not really distinct).

Naming cross-level access as a standalone foundational commitment is what resolves the tension. The levels remain architecturally distinct — cells are cells, aspects are aspects, Selves are Selves. The content-domain relationship remains the typical inter-level pattern. And cross-level access is operationally available, under governance, when purpose requires it. The three commitments compose; they do not collapse into each other.

## 2. The commitment, defined precisely

In the CKS pattern's Self-level architecture, a Self exhibits **cross-level access where purpose requires** if and only if it satisfies five operational properties simultaneously.

**(a) Direct Self-to-cell access is operationally available.** The Self can access cells directly, without routing the access through an aspect's pattern-question machinery, when the deployment configures cross-level access for that purpose. "Access" includes both reads of cell substrate content and writes — the latter subject to all governance commitments named below.

**(b) Aspect-level coordination is bypassed for the access, not eliminated.** The aspects whose cells are accessed directly continue to exist, continue to ask their own pattern questions over their constituent cells, and continue to function as coordination arrangements for other purposes. Cross-level access is a path option, not a structural collapse.

**(c) Cross-level access is enabled per purpose, not by default.** The "where purpose requires" qualifier is operational, not rhetorical. Cross-level access is not the standard mode of Self-to-cell engagement; it is enabled for specific purposes that the deployment names. The default access path is content-domain, through the aspect.

**(d) Cross-level access is configured through orchestration rules.** Which entities can perform cross-level access, on which cells, for which purposes, under which conditions — these questions are answered by orchestration rules authored by humans, in the sense the inherited human-governed commitment names. Cross-level access is not arbitrary; it is patterned.

**(e) Level distinctions are preserved across the access.** A cross-level access does not change the level of the entity performing the access (the Self remains the Self) or of the entity accessed (the cell remains a cell). The access path is what changes; the level structure is what does not.

The five properties together define what the non-strict-hierarchy commitment requires. Failing any one of them — even with the other four robustly satisfied — fails the commitment as Paper 2 specifies it. A system that lets the Self touch cells freely with no rule scaffold (failing (d)) is not exhibiting cross-level access in the CKS sense; it is exhibiting ungoverned access. A system in which Self-to-cell direct access is the only available path (failing (b) or (c)) is not exhibiting non-strict hierarchy; it has eliminated aspects.

## 3. What makes non-strict hierarchy architecturally distinctive

Two architectural neighbors put the commitment's distinctiveness into relief.

**Conventional rigid AI orchestration.** Hierarchical AI orchestration architectures — orchestrators, sub-orchestrators, tool-callers, and so on, organized into strict tiers — typically commit to the property that an orchestrator must reach lower-level components only through its direct subordinates. The whole point of the intermediate tier is that it cannot be bypassed; bypass would violate the architecture's coherence and bypass the contracts the intermediate tier enforces. CKS Self-level architectures permit cross-level access through governed configuration: the Self can decide that for some purposes, going through aspect-level coordination is unnecessary overhead, and access cells directly. The aspects retain their coordination role for the purposes they were designed for; the Self retains the option to bypass them for purposes where their pattern-question machinery would not contribute.

This is operational flexibility, not architectural compromise. The levels remain architecturally distinct (per B1.02). The aspects remain coordination arrangements (per B1.04). The Self remains the integrated whole (per B1.05). What changes is that the access path adapts to purpose, under orchestration rules authored by humans, instead of being fixed by hierarchy.

**Biology.** Biological organisms have largely strict access patterns: signals propagate through tissues to organs to systems to organism-level integration; bypass paths exist but are limited (the autonomic nervous system, hormonal cascades, certain reflex arcs) and are themselves structural — they evolved as fixed bypass channels, not as configurable per-purpose access patterns. CKS exceeds biology on this axis. Where biology has fixed bypass channels with millions-of-years evolutionary timescales, CKS has configurable cross-level access patterns under human governance, modifiable on operational timescales through vertical evolution per B1.16. Paper 2's *Where CKS exceeds biology* discussion names this kind of operational flexibility — structural evolvability on operational timescales, governed per deployment — as a CKS advantage over biological organization.

The biology parallel functions as conceptual scaffold. The architectural substance is configurable bypass under governance.

## 4. The cognitive analog as conceptual scaffold

A cognitive analog parallels the architectural commitment closely enough to function as conceptual scaffold for readers who have not yet absorbed the architectural framing.

Human cognition exhibits something structurally similar to cross-level access. A person engaged in calm-study mode (an aspect, in Paper 2's terms) processes information through that mode's characteristic pattern of attention, working-memory load, and reasoning style. But when the person needs to recall a specific name — say, while writing — they do not process the recall request through "calm-study mode." They access the specific memory directly. The mode of engagement is bypassed for the recall, then re-engaged when the writing resumes. The same person, in competitive-sports mode, may directly access a specific motor-pattern memory without routing the access through the sports mode's broader pattern-question machinery.

This analog is conceptual scaffold, not architectural specification. The architectural substance is configurable bypass-of-intermediate-levels under human governance. The cognitive parallel makes the substance intuitive; the architectural substance is the configurable, governed, audited cross-level access path that orchestration rules per A2.04 specify and provenance per A2.40 records.

## 5. Inherited Paper 1 commitments

Cross-level access does not stand alone as a Paper 2 invention; it inherits Paper 1's commitments and operates within them. Seven inheritance edges are load-bearing.

**A1.01 (human-governed) — cross-level access is governed.** Whether cross-level access is enabled at all, for which purposes, on which cells, under which conditions — these are governance questions answered by orchestration rules authored by humans. Cross-level access does not bypass governance; it is a configurable pattern within governance.

**A2.04 (orchestration rule authoring) — the rules that enable cross-level access are authored by humans.** The "where purpose requires" qualifier is operationalized through orchestration rules: a rule names the purpose, the entities authorized to perform the access, the cells in scope, the operations permitted. The rule is human-authored, version-tracked, and inspectable.

**A1.02 (substrate-cell boundary) — cross-level access does not bypass the boundary.** A direct Self-to-cell access still goes through the cell's substrate boundary. The Self does not reach into a cell's internal state; it reads or writes through the substrate boundary that the cell exposes. The boundary is preserved.

**A1.03 (conflict as first-class) — cross-level writes that conflict register conflicts.** A Self-level direct write that would conflict with cell substrate state does not silently overwrite. The conflict is preserved as first-class substrate state, exactly as a write through aspect coordination would be. Cross-level access does not bypass conflict handling; it interacts with conflict handling on the same terms.

**A1.07 (path retraceability) — cross-level access events are recorded.** Each cross-level access event is recorded with the six provenance metadata fields per A2.40: who performed the access, when, under which orchestration rule, for which purpose, against which cell, with which operation. Cross-level access is auditable on the same terms as any other substrate operation. The audit trail does not have to be reconstructed after the fact; the architecture records it as the access happens.

**A1.10 (determinism contract) — cross-level access is deterministic given configuration.** Given the orchestration rules in force and the substrate state at the time of access, cross-level operations behave deterministically per the configuration. Non-determinism is not introduced by the cross-level path; the same access under the same configuration produces the same effect.

**A2.40 (six provenance metadata fields) — cross-level access provenance is structured.** The provenance fields apply to cross-level access without modification. The "rule" field names the orchestration rule that authorized the cross-level path; the "purpose" field names what the access was for. Cross-level access is not a special audit case; it shares the substrate's standard provenance vocabulary.

The inheritance chain is what makes cross-level access architecturally coherent. Without it, a "Self-to-cell direct access" would be ungoverned bypass — the architectural anti-pattern Paper 2 explicitly does not commit to. With it, cross-level access is a governed pattern: configured, authored, recorded, deterministic, conflict-aware.

## 6. Operational implications

Naming cross-level access as a standalone foundational commitment makes a class of operational scenarios architecturally expressible.

**Efficiency-motivated bypass.** When the aspect's pattern-question machinery would add no value for a specific Self-level purpose — for example, when the Self needs the raw value of a single cell's substrate field, and the aspect's pattern question is over a different field set — cross-level access lets the Self skip the aspect overhead. The aspect retains its coordination role for the purposes that need it; the Self retains the option to bypass when the purpose does not.

**Inspection-motivated bypass.** Self-level audit operations sometimes require cell-level detail that the aspect's pattern question would aggregate, summarize, or filter. A Self that needs to reconstruct exactly what a particular cell wrote, when, and under which rule may need to read the cell directly rather than read an aspect's projection over many cells. Cross-level access makes this inspection path architecturally available.

**Decision-motivated bypass.** Some Self-level decisions depend on cell-level state in ways that the aspect's coordination does not preserve. A Self deciding whether to retire an aspect may need to read the constituent cells' archival state directly, without routing through the aspect that is itself the subject of the decision. The aspect cannot reasonably mediate access to cells whose retirement-readiness it is being evaluated for; the cross-level path is required.

**Emergency-motivated bypass.** When aspect-level coordination is degraded — an aspect's orchestration rules are under revision, an aspect is mid-vertical-evolution restructure, an aspect's pattern questions are returning inconsistent results — the Self may need to interact with the underlying cells without the aspect's intermediation. Cross-level access provides a governed path to do so without abandoning the aspect entirely.

In each of these scenarios, the cross-level access is configured by orchestration rules (per A2.04) that name the purpose, recorded with provenance (per A2.40), and subject to conflict preservation (per A1.03). The scenario is operationally distinct; the architectural commitments are uniform.

Cross-level access patterns themselves evolve through B1.16 vertical evolution. A deployment may add a new cross-level access pattern when a new purpose emerges, modify an existing pattern when a purpose changes, or retire a pattern when its purpose is no longer relevant. Each of these is governed evolution under the standard authority architecture — no new evolutionary primitive is introduced.

The complementarity with content-domain (per B1.18) is the key operational point. Routine inter-level interactions use content-domain — aspects ask pattern questions over their cells; the Self holds aspects as facets. Specific-purpose interactions may use cross-level access when the deployment configures it. The two patterns coexist; deployments use both, choosing which path serves which purpose. Naming both patterns as separate standalone commitments is what allows deployments to think about them separately.

## 7. What cross-level access does NOT do

The standalone treatment is precise. Naming what cross-level access does not do is what keeps the commitment from being read as more permissive than the source paper supports.

**It does not bypass governance.** Cross-level access is configured through human-authored orchestration rules. A "Self-to-cell direct access" outside the rule scaffold is not a CKS cross-level access; it is ungoverned access, which the architecture does not admit.

**It does not bypass the substrate-cell boundary.** A direct Self-to-cell access still reads or writes through the cell's substrate boundary, not through the cell's internal state. A1.02 holds across cross-level access.

**It does not eliminate aspects.** Aspects continue to function as coordination arrangements per B1.04. Cross-level access is an additional path; it does not replace the content-domain path that aspects provide. A Self-level architecture in which aspects exist only nominally, with all access actually routing direct-to-cell, has not implemented cross-level access; it has implemented aspect dissolution and is no longer instantiating Paper 2's three-level structure.

**It does not mean unrestricted access.** "Where purpose requires" is operational. The set of cross-level access paths a deployment makes available is bounded by the orchestration rules; access outside those rules is not "cross-level access," it is unauthorized access, and the substrate's governance commitments treat it as such.

**It does not violate level distinctions.** B1.02 holds across cross-level access. A direct Self-to-cell access does not collapse the cell into the Self or the Self into the cell; cells remain cells, Selves remain Selves. The access path changes; the architectural levels do not.

**It does not bypass conflict handling.** A cross-level write that would conflict with existing cell state registers a conflict, exactly as any other write would. A1.03 holds across cross-level access.

**It does not replace the content-domain relationship.** B1.18 remains the typical inter-level pattern. Cross-level access is the operationally-available alternative for specific purposes; it does not displace the content-domain pattern as the standard mode of inter-level engagement.

The commitment is about access flexibility, not about architectural collapse. A reader who comes away thinking "Paper 2 has no real hierarchy because the Self can access cells directly" has misread the commitment. The hierarchy of levels is real and architecturally distinct; what is not strictly hierarchical is the access pattern across the levels, governed and configured per purpose.

## 8. Operational test

A system instantiates the cross-level-access-where-purpose-requires foundational commitment if and only if all of the following are true.

1. The Self can access cells directly, bypassing aspect-level coordination, when the deployment configures such access for a named purpose.
2. The configuration of cross-level access — which entities, which cells, which purposes, which operations — is specified through orchestration rules authored by humans per the inherited human-governed commitment.
3. Cross-level access events are recorded with the six provenance metadata fields, with the rule and purpose explicitly named in the provenance.
4. Cross-level access does not bypass the substrate-cell boundary; the Self reads or writes through the cell's substrate boundary, not through cell-internal state.
5. Cross-level writes that would conflict with cell substrate state register conflicts as first-class substrate state, on the same terms as writes through aspect coordination.
6. Aspects continue to function as coordination arrangements for the purposes they serve; cross-level access does not eliminate them.
7. The level distinctions among cell, aspect, and Self are preserved across cross-level operations; the access path does not collapse the levels.

A system that fails any of (1)–(7) does not instantiate the commitment as Paper 2 specifies it. Such a system may instantiate something else — a strictly hierarchical orchestrator, an unstructured access surface, a level-collapsing architecture — but it is not instantiating the non-strict-hierarchy property the source paper commits to.

## 9. Conclusion

Cross-level access where purpose requires is what distinguishes Paper 2's three-level structure from rigid hierarchical AI orchestration. Without it, the cell-aspect-Self structure would impose strict access patterns through intermediate layers, and the framework would collapse into a layered orchestrator with the ergonomics of conventional AI hierarchy. With it, the levels remain architecturally distinct, the content-domain relationship remains the typical inter-level pattern, and the access path adapts to purpose under human-authored orchestration rules.

The standalone framing of this commitment matters because the property is operational, not structural. The level distinctions in B1.02, the relational role membership in B1.17, and the content-domain relationship in B1.18 specify the structure of Paper 2's three-level architecture. The non-strict-hierarchy property in B1.19 specifies the access patterns across that structure. The next note in the structural-properties cluster (B1.20) closes Phase B1 by formalizing the recursive commitment — Paper 1's architectural commitments hold at each of the three levels — completing the foundational treatment of Paper 2's three-level architecture.

Subsequent work that adopts, extends, or argues against Paper 2's structural framework should use "cross-level access" in the sense formalized here. Subsequent work that uses the term differently is using a different concept, and the difference should be named.

---

## Source papers

Li, W. (2026). *The Instinct/Reasoning Separation Outside the Model: Extending the Coordination Knowledge Substrate Pattern to AI Selves under Human Governance.* April 2026. ORCID: 0009-0004-8065-3235.

Li, W. (2026). *Coordination Outside the Model: A Human-Governed Substrate Pattern for AI Systems.* April 2026. ORCID: 0009-0004-8065-3235.

## How to cite this note

Li, W. (2026). *Cross-Level Access Where Purpose Requires: Non-Strict Hierarchy as a Foundational Architectural Commitment in the Coordination Knowledge Substrate Pattern's Self-Level Structure.* May 7, 2026. ORCID: 0009-0004-8065-3235.
